// prelude
// https://doc.rust-lang.org/std/prelude/index.html
use std::io;

fn main() {
    let x = 5;
    let y = 10;

    println!("(x, y) = ({x}, {y})");

    println!("Please input your guess.");

    // mutable
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guess: {guess}");
}
