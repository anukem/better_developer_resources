List<string> answer = new List<string>();
void getValidPalindromes(int n, int left, int right, string current)
{
    if (left == n && right == n)
    {
        answer.Add(current);
    }

    if (left <= n)
    {
        getValidPalindromes(n, left + 1, right, current + "(");
    }

    if (right < left)
    {
        getValidPalindromes(n, left, right + 1, current + ")");
    }
}

getValidPalindromes(5, 0, 0, "");
foreach(string a in answer)
{
    Console.WriteLine(a);
}
