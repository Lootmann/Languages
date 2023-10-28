fn main() {
    {
        let a = 10;
        let b = 1;
        println!("{} {}", a, b)
    }

    {
        let a = 10;
        let ma = &a;
        let cp_ma = a;
        println!("{} {} {}", a, ma, cp_ma);
    }

    {
        let mut a = 10;
        a = a + 10;
        let mut_a = &mut a;

        // println!("{}", a);
        println!("{}", mut_a);
    }

    {
        let s = String::from("hello, Rust world :D");
        let len = length(s);
        println!("s length is {}", len);
    }
}

fn length(s: String) -> usize {
    s.len()
}
