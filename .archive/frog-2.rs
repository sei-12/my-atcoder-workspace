#![allow(non_snake_case)]
#![allow(unused)]

use proconio::{input, marker::Chars};
use std::cmp::{max, min};
use std::{collections::VecDeque, i64};

fn main() {
    input! {
        N: usize,
        K: usize,
        H: [i64; N],
    }

    let mut H: VecDeque<_> = H.iter().collect();
    for i in 0..K - 1 {
        H.push_front(H[0]);
    }

    let mut table = vec![0; N + K - 1];
    
    // dbg!(&H);
    // dbg!(&table);

    for n in K..N + K - 1 {
        // dbg!(n,H[n]);
        let mut min_cost = i64::MAX;

        for k in 1..=K {
            min_cost = min(min_cost, table[n - k] + (H[n - k] - H[n]).abs())
        }
        
        table[n] = min_cost;
    }

    println!("{}", table[N + K - 2]);
}
