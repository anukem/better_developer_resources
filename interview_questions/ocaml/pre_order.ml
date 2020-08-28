(* # Write a function that takes a root node as input, and returns a string with the values of the tree in depth first pre-order (root, then left subtree, then right subtree), separated by spaces *)
(* #  *)
(* #  *)
(* # Input 1 *)
(* #         1 *)
(* #         /\ *)
(* #        2  5 *)
(* #       /\  /\ *)
(* #      3 4  6 7 *)
(* #       *)
(* # Input 2 *)
(* #         1 *)
(* #        / \ *)
(* #       2   5 *)
(* #      /   / *)
(* #     3   6 *)
(* #    /   / *)
(* #   4   7 *)
(* #  *)
(* # Input 3 *)
(* #       1 *)
(* #      / \ *)
(* #    401 88 *)
(* #    / *)
(* #  349 *)
(* #  / *)
(* # 90 *)
(* #  *)
(* # Output 1 -> "1 2 3 4 5 6 7" *)
(* # Output 2 -> "1 2 3 4 5 6 7" *)
(* # Output 3 -> "1 401 349 90 88" *)
(* # """ *)

type 'a tree = Node of 'a * 'a tree * 'a tree | Leaf

let dashes n =
let rec helper n =
if n = 0 then "" else if n = 1 then "-" else "-" ^ (helper (n - 1)) in helper n;;

let pre_order tree =
  let rec helper tree n =
    match tree with
    | Leaf ->  ""
    | Node(v, left, right) -> (dashes n) ^ v ^ " " ^ (helper left (n + 1)) ^ " " ^ (helper right (n + 1)) in
   helper tree 0;;

let s = pre_order (Node("laf", Node("dog", Node ("som", Leaf, Leaf), Leaf), Leaf));;
   print_endline s;;
