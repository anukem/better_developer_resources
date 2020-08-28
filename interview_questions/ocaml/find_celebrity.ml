(* You are given a list of n people in a room and your job is to find out if *)
(* there is a celebrity. A celebrity is defined as someone who everyone knows,
   who also knows no one else in the room.

  You are given a helper function knows (a, b) -> bool which will tell you
  whether or not a knows b.

  You will write a function find_celebrity that returns the person that is a
  celebrity if they exist and -1 if they don't. *)
  (* Example 1 ->

     n = 2
     0 knows 1
     1 does not know 2
     2 knows 1
     1 does not know 0

     Answer: 1

     Explanation: 1 knows no one, and everyone knows 1.
  *)


let find_celebrity n knows = let candidate = List.init n (fun x -> x + 1) |>
                                             List.fold_left
                                               (fun acc x -> if knows (x, acc) then acc else x) 0 in
  let validate = List.init n (fun x -> x) |>
  List.fold_left (fun (candidate, is_celebrity) x ->
      if candidate = x then (candidate, is_celebrity) else
      if knows (candidate, x) then (candidate, false) else
        (candidate, is_celebrity)  ) (candidate, true) in
  match validate with
  | (value, true) -> value
  | (value, false) -> (-1)

