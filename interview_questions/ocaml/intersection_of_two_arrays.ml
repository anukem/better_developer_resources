(* you are given two lists a and b and asked to return the intersection of those two lists.

   Examlple 1: [1;2;1] [1;4] -> [1]
   Examlple 2: [1] [2] -> []
   Examlple 3: [1;2;1] [1;2;4] -> [1;2] *)

module MySet = Set.Make(Int)

let intersection_of_two_arrays a b =
  let set = List.fold_left (fun acc el -> MySet.add el acc) MySet.empty a in
  let set' = List.fold_left (fun acc el -> MySet.add el acc) MySet.empty b in
  let result = MySet.inter set set' in
  MySet.elements result




