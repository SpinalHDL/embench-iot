/* Copyright (C) 2017 Embecosm Limited and University of Bristol

   Contributor Graham Markall <graham.markall@embecosm.com>

   This file is part of Embench and was formerly part of the Bristol/Embecosm
   Embedded Benchmark Suite.

   SPDX-License-Identifier: GPL-3.0-or-later */

#include <support.h>

void
initialise_board ()
{

}

#define capture_cycle(key) *((unsigned int*)0xF00FFF50) = key;
#define sim_end()  *((unsigned int*)0xF00FFF20) = 0;
static unsigned int time;
void __attribute__ ((noinline)) __attribute__ ((externally_visible))
start_trigger ()
{
    capture_cycle(1);
}

void __attribute__ ((noinline)) __attribute__ ((externally_visible))
stop_trigger ()
{
    capture_cycle(2);
    sim_end();
}
