#include <math.h>

#ifndef ONLINE_JUDGE
#define _GLIBCXX_DEBUG
#endif




// 可変長引数マクロの定義
#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME

/**
 * @brief 可変長引数マクロを使用して、Pythonのrangeのような挙動を提供します。
 * @param i ループカウンタ変数。各ループで指定された範囲の値を持ちます。
 * @param end 終了値。ループはこの値より小さい間繰り返されます (step > 0 の場合)。
 * @param start 開始値 (オプション)。デフォルトは 0。
 * @param step 増分値 (オプション)。デフォルトは 1。負の値を指定すると降順のループを実現できます。 0 の場合は無限ループになります。適切な値を設定してください。
 */
#define rep(...) GET_MACRO(__VA_ARGS__, range3, range2, range1)(__VA_ARGS__)

// range(start, end, step)
#define range3(i, start, end, step) \
    for (int i = (start); ((step) > 0 ? i < (end) : i > (end)); i += (step))

// range(start, end) -> デフォルトで step = 1
#define range2(i, start, end) \
    for (int i = (start); i < (end); i++)

// range(end) -> デフォルトで start = 0, step = 1
#define range1(i, end) \
    for (int i = 0; i < (end); i++)



using ll = long long;
using ld = long double;
using namespace std;

/**
 * @brief Calculates the Euclidean distance from the origin to a point (a, b).
 *
 * This function computes the distance using the Pythagorean theorem:
 *     distance = sqrt(a^2 + b^2)
 *
 * @param a The x-coordinate (long double).
 * @param b The y-coordinate (long double).
 * @return The Euclidean distance as a long double.
 */
inline long double euclidean_distance(
    long double a,
    long double b
){
    return sqrt( a * a + b * b );
}

// -- mylib -- //