(* Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
   An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
   You may assume all four edges of the grid are all surrounded by water. *)
(*  *)
(*   *)
(*  *)
(* Example 1: *) (*  *)
(* Input: grid = [ *)
  (* ["1","1","1","1","0"], *)
  (* ["1","1","0","1","0"], *)
  (* ["1","1","0","0","0"], *)
  (* ["0","0","0","0","0"] *)
(* ] *)
(* Output: 1 *)
(* Example 2: *)
(*  *)
(* Input: grid = [ *)
(*   ["1","1","0","0","0"], *)
(*   ["1","1","0","0","0"], *)
(*   ["0","0","1","0","0"], *)
(*   ["0","0","0","1","1"] *)
(* ] *)
(* Output: 3

   get the tawble
   for each node
   mark as visited
   go to neighbor
*)

module IntInt = struct
  type t = int * int
  let compare = compare
end

module MySet = Set.Make(IntInt)

let make_table grid =
  let table = Hashtbl.create 100 in
  let rec columns x y lst =
    match lst with
    | [] -> ()
    | h::tl -> (Hashtbl.add table (x, y) h); columns x (y + 1) tl in

  let rec rows x g =
  match g with
  | [] -> ()
  | h::tl -> columns x 0 h ; rows (x + 1) tl in

  rows 0 grid; table

let rec mark_neighbors t visited (x, y) =
  let visited = MySet.add (x, y) visited in
  let neighbors = List.filter (
  fun point ->
      match Hashtbl.find_opt t point with
      | None -> false
      | Some x -> if x = 1
        then match MySet.find_opt point visited with
          | None -> true
          | Some x -> false
        else false
    ) [(x + 1, y); (x - 1, y); (x, y - 1); (x, y + 1)] in
  let ret = List.fold_left (fun acc current_neighbor ->
      (MySet.union (mark_neighbors t (MySet.add current_neighbor acc) current_neighbor) acc)) visited neighbors
  in ret

let ones_ tbl = Hashtbl.filter_map_inplace (fun (x, y) value -> match value with 1 -> Some value | _ -> None) tbl

let num_islands lst =
  let table = make_table lst in
    let add_island (x, y) value (visited, islands) =
      let new_visited = mark_neighbors table visited (x, y) in
          match MySet.equal visited new_visited with
          | true -> (visited, islands)
          | false -> (MySet.union visited new_visited, islands + 1) in
  ones_ table;
  Hashtbl.fold add_island table (MySet.empty, 0) |> snd
