use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    // [1,101) (1,101)
    //         (1..101)
    //         (1..=100)
    println!("random number = {}", rng.gen_range(1..=6));
}