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

#define read_cycles() (*((unsigned int*)0xf001BFF8))
static unsigned int time;
void __attribute__ ((noinline)) __attribute__ ((externally_visible))
start_trigger ()
{
    time = read_cycles();
}

void __attribute__ ((noinline)) __attribute__ ((externally_visible))
stop_trigger ()
{
  time = read_cycles()-time;
  __asm__ volatile ("ebreak");
}
