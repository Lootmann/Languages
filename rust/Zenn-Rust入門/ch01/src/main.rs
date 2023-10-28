fn main() {
    {
        title(String::from("int ownership"));
        let x: i32 = 1;
        let y = x;

        ownership(x);
        ownership(y);

        println!("{} {}", x, y);
    }

    {
        title(String::from("String ownership"));
        let s1 = String::from("hello");
        let s2 = s1; // move s1 to s2
        println!("{}", s2);

        // take_ownerships(s2);
        // println!("{}", s2);

        take_ownerships(s2.clone());
        println!("{}", s2);
    }

    {
        title(String::from("Reference and Mutation"));
        let s = String::from("hello");

        // 参照を渡す
        let len = length(&s);
        println!("The length of {} is {}.", s, len)
    }

    {
        title(String::from("Variable Reference"));
        let mut s = String::from("hello");
        let mut s1 = &mut s;
        change(&mut s1); // 可変な参照を渡す 危険な行為

        println!("{}", s1);
    }
}

fn title(s: String) {
    println!("\n+-+-+ {} +-+-+", s);
}

fn take_ownerships(s: String) {
    println!("* in take_ownerships {}", s);
}

fn ownership(i: i32) {
    println!("- in ownership {}", i);
}

// 参照を受け取る
fn length(s: &String) -> usize {
    // doesn't work, Reference is also immutable!
    // s.push_str("hoge");
    s.len()
    // s はただの参照、所有権は持っていないのでDropは発生し得ない
}

fn change(string: &mut String) {
    // 可変 則ち 変更可能
    string.push_str(", Rust world !");
}
