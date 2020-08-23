(* A peak element is an element that is greater than its neighbors. *)
(*  *)
(* Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index. *)
(*  *)
(* The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. *)
(*  *)
(* You may imagine that nums[-1] = nums[n] = -∞. *)
(*  *)
(* Example 1: *)
(*  *)
(* Input: nums = [1,2,3,1] *)
(* Output: 2 *)
(* Explanation: 3 is a peak element and your function should return the index number 2. *)
(* Example 2: *)
(*  *)
(* Input: nums = [1,2,1,3,5,6,4] *)
(* Output: 1 or 5  *)
(* Explanation: Your function can return either index number 1 where the peak element is 2,  *)
(*              or index number 5 where the peak element is 6. *)
(* Follow up: Your solution should be in logarithmic complexity *)

let n_solution lst =
	let rec helper i lst =
		match lst with
		| h::h2::h3::tl -> if h2 > h && h2 > h3 then i + 1 else helper (i + 1) (h2::h3::tl)
		| _ -> -1
	in helper 0 lst

let find_peak_element lst =
	let rec search left right lst =
    if left >= right then left else
    (let mid = left + (right - left) / 2 in
      if List.nth lst mid < List.nth lst (mid + 1) then search (mid + 1) right lst else search left mid lst) in
  search 0 (List.length lst) lst
