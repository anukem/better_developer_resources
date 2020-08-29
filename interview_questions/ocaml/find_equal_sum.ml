(* Given a non empty array containing only positive integers *)
(*   find if the array can be partitioned into two subsets *)
(*     such that the sum of both subsets are equal. *)

(* Example 1: [1;5;11;5] -> true *)
(* Example 2: [1;5;2;5] -> false *)


let find_equal_sum lst = let sum = List.fold_left (+) 0 lst in
  let mid = sum / 2 in
  let rec helper amount_left lst =
  if (sum mod 2) = 0 then (match lst with
    | [] -> false
    | h::tl -> if amount_left = 0 then true
               else if amount_left < 0 then false
               else (helper amount_left tl) ||  helper (amount_left - h) tl) else false in
      helper mid lst
