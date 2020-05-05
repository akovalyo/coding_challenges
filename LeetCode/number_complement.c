int	bin_count(int nbr)
{
	if (nbr >= 2)
		return (1 + bin_count(nbr / 2));
	return(1);
}

int findComplement(int num)
{
    return (num ^ ((long)pow(2, bin_count(num)) - 1));
}