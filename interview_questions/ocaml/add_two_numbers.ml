(* 2. Add Two Numbers *)
(* Medium *)
(*  *)
(* 8899 *)
(*  *)
(* 2246 *)
(*  *)
(* Add to List *)
(*  *)
(* Share *)
(* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. *)
(*  *)
(* You may assume the two numbers do not contain any leading zero, except the number 0 itself. *)
(*  *)
(* Example: *)
(*  *)
(* Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) *)
(* Output: 7 -> 0 -> 8 *)
(* Explanation: 342 + 465 = 807. *)
(* Accepted *)
(* 1,498,934 *)
(* Submissions *)
(* 4,413,074 *)


let add_two_numbers lst1 lst2 =
  let rec helper lst1 lst2 remainder result =
    match lst1, lst2 with
    | [], [] -> result
    | h::tl, [] | [] , h::tl -> if h + remainder >= 10 then helper tl [] 1 ((h + remainder) mod 10::result) else helper tl [] 0 ((h + remainder)::result)
    | h::tl, x::xs -> if h + x + remainder >= 10 then helper tl xs 1 (((h + x + remainder) mod 10)::result) else helper tl xs 0 ((h + x + remainder)::result)
  in List.rev (helper lst1 lst2 0 [])
