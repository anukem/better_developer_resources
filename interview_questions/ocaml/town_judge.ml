(* In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge. *)
(*  *)
(* If the town judge exists, then: *)
(*  *)
(* The town judge trusts nobody. *)
(* Everybody (except for the town judge) trusts the town judge. *)
(* There is exactly one person that satisfies properties 1 and 2. *)
(* You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b. *)
(*  *)
(* If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1. *)
(*  *)
(*   *)
(*  *)
(* Example 1: *)
(*  *)
(* Input: N = 2, trust = [[1,2]] *)
(* Output: 2 *)
(* Example 2: *)
(*  *)
(* Input: N = 3, trust = [[1,3],[2,3]] *)
(* Output: 3 *)
(* Example 3: *)
(*  *)
(* Input: N = 3, trust = [[1,3],[2,3],[3,1]] *)
(* Output: -1 *)
(* Example 4: *)
(*  *)
(* Input: N = 3, trust = [[1,2],[2,3]] *)
(* Output: -1 *)
(* Example 5: *)
(*  *)
(* Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]] *)
(* Output: 3 *)
(*   *)
(*  *)
(* Constraints: *)
(*  *)
(* 1 <= N <= 1000 *)
(* 0 <= trust.length <= 10^4 *)
(* trust[i].length == 2 *)
(* trust[i] are all different *)
(* trust[i][0] != trust[i][1] *)
(* 1 <= trust[i][0], trust[i][1] <= N *)
(*  *)

module Set = Set.Make(Int)

  (* returns:  [from i j l] is the list containing the integers from
 *   [i] to [j], inclusive, followed by the list [l].
 * example:  [from 1 3 [0] = [1;2;3;0]] *)
let rec from i j l =
  if i>j then l
  else from i (j-1) (j::l)

(* returns:  [i -- j] is the list containing the integers from
 *   [i] to [j], inclusive.
 *)
let (--) i j =
  from i j []

let print_set s = Set.iter (fun x -> print_int x; print_string "\n") s

let find_judge n trust =
  let possibleJudges = List.fold_right Set.add (1 -- n) Set.empty in
  let trustsSomeone = List.fold_right Set.add (List.map (fun x ->
      match x with h::tl -> h | [] -> failwith "bad trust relationship") trust) Set.empty in
  let diff = Set.diff possibleJudges trustsSomeone in
  match List.length (Set.elements diff) with
  | 0 -> -1
  | 1 -> let trusters = List.filter (fun x -> match x with h::s::tl -> s = (Set.choose diff) | _ -> failwith "not possible" ) trust |> List.length in
    if trusters = (n-1) then Set.choose diff
    else -1
  | _ -> -1
