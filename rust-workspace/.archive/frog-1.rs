#![allow(non_snake_case)]
#![allow(unused)]

use std::collections::VecDeque;
use proconio::{input, marker::Chars};
use std::cmp::{max, min};

fn main() {
    input! {
        N: usize,
        H: [i64; N],
    }

    let mut H: VecDeque<_> = H.iter().collect();
    H.push_front(H[0]);

    let mut table = vec![0; N + 1];

    for n in 2..N + 1 {
        table[n] = min(
            table[n-1] + (H[n-1] - H[n]).abs(),
            table[n-2] + (H[n-2] - H[n]).abs(),
        )
    }

    println!("{}", table[N]);
}
