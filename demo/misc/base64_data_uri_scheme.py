#Data URI scheme  
#RFC2397
#html中使用 <img src="data:image/png;base64,iVB...==">

"""   
data:[<mediatype>][;base64],<data>

data:                         文本数据
data:text/plain               文本数据
data:text/html                HTML代码
data:text/html;base64         base64编码的HTML代码
data:text/css                 CSS代码
data:text/css;base64          base64编码的CSS代码
data:text/javascript          Javascript代码
data:text/javascript;base64   base64编码的Javascript代码
data:image/gif;base64         base64编码的gif图片数据
data:image/png;base64         base64编码的png图片数据
data:image/jpeg;base64        base64编码的jpeg图片数据
data:image/x-icon;base64      base64编码的icon图片数据 

示例
data:text/html,<script>alert('hi');</script>   
"""

#Data URI scheme 转换成文件
import base64

src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAhdEVYdENyZWF0aW9uIFRpbWUAMjAxOTowNDoyMyAxMjoyNToxMw4lxZUAAAQ5SURBVEhLtZfJK/1RFMDPe4ZknmdJxkiShViIlJUyLBR/AbJSFFkosrCThVhZ2iglC5GhKIkkQ2aZ53kez++c8+7zHt7AD5/yfO+59/s933vG+9UgAV/g9vYWbm5uwMbGBi4vL+Hp6UnkWq0W3N3d4fX1Fezt7cHNzU3k1rCqmBUuLi6Cl5cXODk5AS/39vZWszrOzs7g5eVFXmZ/fx+CgoLA19dXzZrGrGLe3e7uruwoPDxcSb/G0dERHBwcQHBwsFjDJKz4I1dXVzg1NYUPDw9K8n+QpXBzc1ON3vNpx2yq09NTiI2NVZKfcXh4CMfHx5+fJ+oVFxcXODs7q0a/B5keV1ZW1EiHVumH6+troEmIi4tTkt9DH4y88zfUC+D8/PyPfWqNyclJdaV2TCYGBwcHycO/JCoqSqzKiOLV1VUICwsTgTVOTk6gtLQUioqKYHx8XIrJV3F2dgayqtQCDd3IQSU5ZwlWWFFRAV1dXWIhCkJYX1+Hvr4+qVa1tbVqpWXYz1xsONyRBjrDm4D9kpmZieQG9PPzQ7IM+vj44MjIiFqB2Nvbi5GRkdjU1ISUikpqGs4cKi6o1Wg0Up0+Mjw8DBkZGVBXVyeV6PHxERwdHaVWM/QM+c9kZWXB0tKS1AD2Y3l5uZr5jKurK5yfn4OWfzw8PETItbajo0NSKj09HUZHRyE5ORmmp6ehs7MT+CW5FDLGivU0NDTIS97d3cnasrIy2NjYULMGZLP8w9TX10NKSgoUFhZK4PT390ud5Ycw+fn5QGUUqqqqxN+WaGlpEYXsz6SkJCgoKJB7KisrJS44e7S2trYwMzMDPT09QHVVbvT09ITExERISEh4a38Mmyk3NxdCQkLeyU1BcSBKWeHCwgK0trZKKrGrxFpcyPUsLy9jcXEx+vv7I/kTyffY2Ngoc3t7e5iWliZyegEcGhoSuSna2tokGKmV4sDAgJIaYD3sM4m0j1RXVyOlGObl5SH5ih0q44iICCSL4ODgoFppoLu7GwMDA5F2ihMTE0r6Gd6sxXSiBo9kIqQ4QApAJBOLYr42Vry2toYUjJidnY1UVJTUNNQTxHp8ekBq+Epsnvb2dkxNTRXzs7lZAb90TU0N5uTk4Pb2tlppGb6H0g6lSRgXb0s8Pz/j2NgY0okES0pKsLm5Wcz2HSjfkWqCTjH7mbf/11Am4NzcnFxLyeKDGeccjXn4Z3Da6k8ib7UyNDQUqCer0e9DFoWAgAA1MlLs4uIiJwV9EflN7u/vxaJUH5TESDFD3Uda1s7OjpL8HC65bMn4+Hgl0WHyXM1dhntudHS0kvwfvAE6KkNMTIySGDB7oOeTxdbWlgQe193vwB8DXJepipm91+onDLdBDgw+oXAn40ZhZ2enZnXwI/gzhuf564OPOByslrCqWA8f8hn+ltKfm/iPuxsr5ODkD7evWQfgHwaknlJZPxj0AAAAAElFTkSuQmCC"

file="favicon.png"

data = src.split(",")[1]
image_data = base64.b64decode(data)

with open(file, "wb") as f:
    f.write(image_data)


##############################################
#文件转换成Data URI scheme

import base64
file="favicon.png"
scheme_type="data:image/gif;base64"

with open(file, "rb") as f:
    image_data=f.read()

base64_str=base64.b64encode(image_data).decode('utf8')

scheme_data=scheme_type+","+base64_str

print(scheme_data)
    
