#![allow(non_snake_case)]
#![allow(unused)]

use itertools::Itertools;
use proconio::{
    input,
    marker::{Chars, Usize1},
};
use std::collections::{BinaryHeap, HashMap, VecDeque};

#[rustfmt::skip]
fn max<T: Ord>(a: T, b: T) -> T { if a > b { a } else { b } }
#[rustfmt::skip]
fn min<T: Ord>(a: T, b: T) -> T { if a < b { a } else { b } }


fn main() {
    input! {
        N: usize,
        A: [usize; N],
    }
}
