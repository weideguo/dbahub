from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key!"     # 用于 SocketIO，生产环境需更换
socketio = SocketIO(app, cors_allowed_origins="*") 

# 存储房间信息（简化，实际应用需更健壮的存储）
# 这里我们假设一个房间只有两个用户
rooms = {}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("join")
def handle_join(data):
    """客户端请求加入一个房间"""
    room = data["room"]
    join_room(room) 
    print(f"Client {request.sid} joined room {room}")

    # 如果房间已有用户，则通知他们新用户加入
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(request.sid)

    # 通知房间内所有其他成员有新用户加入
    emit("user_joined", {"room": room, "new_user_id": request.sid}, room=room, include_self=False)

@socketio.on("leave")
def handle_leave(data):
    """客户端离开房间"""
    room = data["room"]
    leave_room(room)
    if room in rooms and request.sid in rooms[room]:
        rooms[room].remove(request.sid)
        if len(rooms[room]) == 0:
            del rooms[room]
    print(f"Client {request.sid} left room {room}")
    # 通知房间内其他成员
    emit("user_left", {"room": room, "user_id": request.sid}, room=room, include_self=False)

@socketio.on("signal")
def handle_signal(data):
    """
    处理信令消息（SDP offer/answer, ICE candidates）
    将消息转发给房间内的其他用户
    """
    room = data["room"]
    target_user_id = data.get("target_user_id") # 指定转发给谁（房间内）
    signal_data = data["signal_data"] # 包含 type (offer, answer, candidate), sdp 或 candidate 信息
    sender_id = request.sid

    # 将信令消息转发给目标用户（或房间内所有其他用户）
    # 这里简单地发给房间内所有其他用户
    emit("signal", {"sender_id": sender_id,"signal_data": signal_data}, room=room, include_self=False)

    print(f"Signal from {sender_id} to room {room}: { signal_data.get('type', 'candidate') }")

@socketio.on("disconnect")
def handle_disconnect():
    """处理客户端断开连接"""
    print(f"Client {request.sid} disconnected")
    # 
    for room, user_ids in rooms.items():
        if request.sid in user_ids:
            user_ids.remove(request.sid)
            if len(user_ids) == 0:
                del rooms[room]
            # 通知房间内其他成员
            emit("user_left", {"room": room, "user_id": request.sid}, room=room)
            break

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)