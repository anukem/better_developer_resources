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
