(*  Sorted Lists *)
(* Easy *)
(*  *)
(* 4682 *)
(*  *)
(* 611 *)
(*  *)
(* Add to List *)
(*  *)
(* Share *)
(* Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists. *)
(*  *)
(* Example: *)
(*  *)
(* Input: 1->2->4, 1->3->4 *)
(* Output: 1->1->2->3->4->4 *)
(* Accepted *)
(* 1,071,419 *)
(* Submissions *)
(* 1,994,152 *)

let merge_sort lst1 lst2 =
  let rec helper lst1 lst2 final =
    match lst1, lst2 with
    | [], [] -> final
    | [], h::tl | h::tl, [] -> helper [] tl (h::final)
    | h::tl, x::xs -> if h >= x then helper (h::tl) xs (x::final) else helper tl (x::xs) (h::final)
  in List.rev (helper lst1 lst2 [])

