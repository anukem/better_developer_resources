(* Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
   An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
   You may assume all four edges of the grid are all surrounded by water. *)
(*  *)
(*   *)
(*  *)
(* Example 1: *) (*  *)
(* Input: grid = [ *)
(*   ["1","1","1","1","0"], *)
(*   ["1","1","0","1","0"], *)
(*   ["1","1","0","0","0"], *)
(*   ["0","0","0","0","0"] *)
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

let gen n = List.init n (fun x -> x)

let print_table table =
  let max_x = Hashtbl.fold (fun (x, _) _ init -> if x > init then x else init ) table 0 in
  let max_y = Hashtbl.fold (fun (_, y) _ init -> if y > init then y else init ) table 0 in

  List.map (fun x -> List.map (fun y ->
      print_string (List.fold_left (^) "" ["(";string_of_int x;",";string_of_int y;")"; " "; string_of_int (Hashtbl.find table (x, y) );"\n"])) (gen (max_y + 1)) ) (gen (max_x + 1) )
|> (fun r -> ())

let print_pair (x, y) =
  print_string (string_of_int x);
  print_string ",";
  print_string (string_of_int y);
  print_string "\n"

let rec mark_neighbors t visited (x, y) =
  print_pair (x, y);
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
  List.fold_left (fun acc current_neighbor -> (MySet.union (mark_neighbors t (MySet.add current_neighbor visited) current_neighbor) acc)) MySet.empty neighbors


let num_islands lst =
  let table = make_table lst in
  mark_neighbors table MySet.empty (0, 0)


