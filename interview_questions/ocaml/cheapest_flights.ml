(* 787. Cheapest Flights Within K Stops *)
(* Medium *)
(*  *)
(* 2201 *)
(*  *)
(* 74 *)
(*  *)
(* Add to List *)
(*  *)
(* Share *)
(* There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w. *)
(*  *)
(* Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1. *)
(*  *)
(* Example 1: *)
(* Input:  *)
(* n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]] *)
(* src = 0, dst = 2, k = 1 *)
(* Output: 200 *)
(* Explanation:  *)
(* The graph looks like this: *)
(*  *)
(*  *)
(* The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture. *)
(* Example 2: *)
(* Input:  *)
(* n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]] *)
(* src = 0, dst = 2, k = 0 *)
(* Output: 500 *)
(* Explanation:  *)
(* The graph looks like this: *)
(*  *)
(*  *)
(* The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture. *)
(*   *)
(*  *)
(* Constraints: *)
(*  *)
(* The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1. *)
(* The size of flights will be in range [0, n * (n - 1) / 2]. *)
(* The format of each flight will be (src, dst, price). *)
(* The price of each flight will be in the range [1, 10000]. *)
(* k is in the range of [0, n - 1]. *)
(* There will not be any duplicated flights or self cycles. *)


module MyMap = Map.Make(Int)

let min_list lst = let minimium = List.fold_left (fun acc value -> min acc value) max_int lst in if minimium = max_int then (-1) else minimium

let cheapest_flights flights src dst k =
  let succ = List.fold_left (fun map (src, dst, cost) -> MyMap.add src [] map ) MyMap.empty flights in
  let succ =  List.fold_left (fun map (src, dst, cost) -> MyMap.add src ((dst, cost)::(MyMap.find src map)) map ) succ flights in
  let rec find_shortest_path map src dst cost k =
    if src = dst && k >= 0 then cost
    else if k = 0 then max_int
    else let total_cost = List.fold_left (fun acc (new_destination, c) -> (find_shortest_path map new_destination dst (cost + c) (k - 1) )::acc) [] (match MyMap.find_opt src map with None -> [] | Some x -> x) in
  match total_cost with
  | [] -> max_int
  | lst -> min_list lst in
find_shortest_path succ src dst 0 (k + 1)

