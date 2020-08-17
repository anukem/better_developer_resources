(* In a given grid, each cell can have one of three values: *)
(*  *)
(* the value 0 representing an empty cell; *)
(* the value 1 representing a fresh orange; *)
(* the value 2 representing a rotten orange. *)
(* Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten. *)
(* Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead. *)

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

let hasRottenNeighbors x y table =
  let neighbors = [(x + 1, y); (x - 1, y); (x, y -1); (x, y + 1)] in
  List.map (fun neighbor -> match Hashtbl.find_opt table neighbor with
          | None -> false
          | Some x -> if x = 2 then true else false) neighbors |> List.exists (fun x -> x = true)

let update_table table =
  let table_copy = Hashtbl.create (Hashtbl.length table) in
  Hashtbl.iter (fun (x, y) value ->
      if value = 0 || value = 2 then Hashtbl.add table_copy (x, y) value
      else if hasRottenNeighbors x y table then Hashtbl.add table_copy (x, y) 2 else Hashtbl.add table_copy (x, y) 1) table ; table_copy

let gen n = List.init n (fun x -> x)

let print_table table =
  let max_x = Hashtbl.fold (fun (x, _) _ init -> if x > init then x else init ) table 0 in
  let max_y = Hashtbl.fold (fun (_, y) _ init -> if y > init then y else init ) table 0 in

  List.map (fun x -> List.map (fun y ->
      print_string (List.fold_left (^) "" ["(";string_of_int x;",";string_of_int y;")"; " "; string_of_int (Hashtbl.find table (x, y) );"\n"])) (gen (max_y + 1)) ) (gen (max_x + 1) )

  (* Hashtbl.iter (fun (x, y) value -> *)
  (*   print_string (List.fold_left (^) "" ["(";string_of_int x;",";string_of_int y;")"; " "; string_of_int value;"\n"]) ) table *)

let rottingOranges grid =
  let table = make_table grid in
  let rec update t n =
    match Hashtbl.fold (fun (x, y) value init -> init || (value = 1 && (hasRottenNeighbors x y t ))) t false with
    | true -> update (update_table t) (n + 1)
    | false -> if Hashtbl.fold (fun _ value init -> init || value = 1 ) t false then -1 else n in

  update table 0

