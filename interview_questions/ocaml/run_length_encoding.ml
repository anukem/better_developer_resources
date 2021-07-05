type 'a rle =
    | One of 'a
    | Many of int * 'a

let encoding l =
  let rec aux count acc = function
  | [] -> []
  | [x] -> (count + 1, x)::acc
  | a::(b::_ as t) -> if a = b then aux (count + 1) acc t else aux 0 ((count + 1, a)::acc) t
  in
  List.rev (aux 0 [] l)

let decode l =
  let rec aux acc = function
    | [] -> acc
    | (One h)::t -> aux (h::acc) t
    | Many (c, v)::t -> if c > 0 then aux (v::acc) ((Many (c - 1, v))::t) else aux acc t
  in List.rev (aux [] l)
