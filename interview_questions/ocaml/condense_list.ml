(* 9. Pack consecutive duplicates of list elements into sublists. (medium) *)
let condense_list x =
  let rec aux total current = function
    | [] -> []
    | [y] -> (y::current)::total
    | a::(b::_ as t) -> if a = b then aux total (a::current) t else aux ((a::current)::total) [] t
  in List.rev (aux [] [] x)


