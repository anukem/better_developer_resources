(* 322. Coin Change *)
(* Medium *)
(*  *)
(* 4670 *)
(*  *)
(* 145 *)
(*  *)
(* Add to List *)
(*  *)
(* Share *)
(* You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. *)
(*  *)
(* Example 1: *)
(*  *)
(* Input: coins = [1, 2, 5], amount = 11 *)
(* Output: 3  *)
(* Explanation: 11 = 5 + 5 + 1 *)
(* Example 2: *)
(*  *)
(* Input: coins = [2], amount = 3 *)
(* Output: -1 *)
(* Note: *)
(* You may assume that you have an infinite number of each kind of coin. *)

let rec min_list lst =
  match lst with
  | [] -> max_int
  | h::tl -> if h < min_list tl then h else min_list tl

 let coin_change lst amt =
  let coins = List.sort (fun a b -> b - a) lst in
  let rec helper coins amt dec_amt =
    match coins with
    | [] -> (-1)
    | h::tl -> match amt > 0 with
      | true -> min_list (List.map (fun el -> helper coins (amt - el) (dec_amt + 1) ) coins)
      | false -> if amt = 0 then dec_amt else max_int in
  if helper coins amt 0 = max_int then (-1) else helper coins amt 0
