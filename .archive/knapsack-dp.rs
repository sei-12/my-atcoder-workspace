#![allow(non_snake_case)]
#![allow(unused)]

use std::{cmp::max, collections::VecDeque};

use proconio::{input, marker::Chars};

fn main() {
    input! {
        N: usize,
        W: usize,
        mut WV: [(usize,usize); N],
    }

    let mut WV: VecDeque<_> = WV.into_iter().collect();
    WV.push_front((0,0));

    let mut table = vec![vec![0; W+1]; N+1];
    
    for i in 1..N+1 {
        for w in 0..W+1 {
            let wi = WV[i].0;
            let vi = WV[i].1;

            if w < wi {
                table[i][w] = table[i-1][w];
                continue;
            }
            
            table[i][w] = max(
                table[i-1][w],
                table[i-1][w - wi] + vi
            )
        }
    }
    
    println!("{}",table[N][W]);
}
