#!/bin/bash
assumptions=$(cat assumptions.txt)
counter=0
output_file=problems.out
START='============================== PROOF ================================='
END='============================== end of proof =========================='

while IFS= read -r goal; do
  echo "
    formulas(assumptions).
    $assumptions
    end_of_list.

    formulas(goals).
    $goal
    end_of_list." > problems.in

    ((counter=counter+1))
    output_file=problem$counter.out
    echo $counter. $goal
    echo ""
    prover9 -f problems.in > $output_file
    sed -n "/^$START/,/^$END/p;" $output_file
    echo ""

done < ./goals.txt