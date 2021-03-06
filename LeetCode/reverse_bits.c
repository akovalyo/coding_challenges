/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_bits.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alex <alex@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/04/07 20:12:59 by akovalyo          #+#    #+#             */
/*   Updated: 2020/09/17 16:38:24 by alex             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdint.h>

uint32_t reverseBits(uint32_t n) 
{
    int				i;
	uint32_t	    new;

	i = 0;
	new = 0;
	while (i < 32)
	{
		new |= (((n >> i) & 1) << (31 - i));
		i++;
	}
	return (new);
    
}
