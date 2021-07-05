let replicate l n =
  let rec aux acc count = function
    | [] -> acc
    | h::t -> if count > 0 then aux (h::acc) (count - 1) (h::t) else aux acc n t
  in List.rev (aux [] n l)
