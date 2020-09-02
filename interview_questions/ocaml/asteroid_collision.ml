(* We are given an array *asteroids* of integers representing asteroids in a row.
   For each asteroid teh absolite value represents its size and the sign represents its direction.
   Each asteroid moves at the same speed.

   Find out the state of the asteroids after all collisions. If two asteroids mee, the smaller one will
   explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

   Example 1: [5, 10, -5] -> [5, 10]
   Example 2: [5, -5] -> []
   *)

let rec print_list = function
[] -> "\n"
| e::l -> (string_of_int e) ^ " " ^ print_list l

module MyStack = Stack.Make(Int)

(* let asteroid_collision lst = *)
(*   let stack = MyStack.empty in *)
(*   List.map (fun el -> MyStack.fold (fun acc other_element -> ) ) *)
