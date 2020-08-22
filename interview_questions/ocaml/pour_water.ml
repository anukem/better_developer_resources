(* See pour_water.py for description *)

(* takes a list of numbers and adds a droplet if possible *)
(*     to the left of the k *)
let go_left heights k =
  let rec go i k =
    match (-1) != i && heights.(i) <= heights.(k) with
    | true ->
      if heights.(i) < heights.(i + 1)
      then (heights.(i) <- (heights.(i) + 1); (i, true, heights))
      else go (i - 1) k
    | false -> (i, false, heights) in
  go (k - 1) k


(* takes a list of numbers and adds a droplet if possible *)
(*     to the right of the k *)
let go_right heights k =
  let rec go i k =
    match i != Array.length heights && heights.(i) <= heights.(k) with
    | true ->
      if heights.(i) < heights.(i - 1) then
        (heights.(i) <- (heights.(i) + 1); (i, true, heights))
      else (go ( i + 1 ) k)
    | false -> (i, false, heights) in
  go (k + 1) k


let rec pour_water heights k v =
  match v = 0 with
  | true -> heights
  | false -> match go_left heights k with
    | (i, true, h) -> pour_water h k (v - 1)
    | (i, false, h) -> match go_right h k with
      | (i, true, h) -> pour_water h k (v - 1)
      | (i, false, h) -> h.(k) <- h.(k) + 1; pour_water h k (v - 1)
