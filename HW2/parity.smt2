; Boolean parity function over four variables
; variables {p1,p2,p3,p4} - Three equivalent

(declare-const p1 Bool)
(declare-const p2 Bool)
(declare-const p3 Bool)
(declare-const p4 Bool)



(declare-const a Bool)
(declare-const b Bool)

(declare-fun lrarrow (Bool Bool) Bool)
(assert (= (lrarrow a b)
	   	  (and (=> a b) (=> b a))))

(declare-fun BICON (Bool Bool Bool Bool) Bool)
(assert (= (BICON p1 p2 p3 p4)
        (lrarrow (lrarrow (lrarrow p1 p2) p3) p4)))




(declare-fun CNF (Bool Bool Bool Bool) Bool)
(assert (= (CNF p1 p2 p3 p4)
           (and
		(or (not p1) (not p2) (not p3) p4)
	   	(or (not p1) (not p2) p3 (not p4))
	   	(or (not p1) p2 (not p3) (not p4))
	       	(or (not p1) p2 p3 p4)
	   	(or p1 (not p2) (not p3) (not p4))
	   	(or p1 (not p2) p3 p4)
	   	(or p1 p2 (not p3) p4)
	   	(or p1 p2 p3 (not p4)))
	   )
	)


(declare-fun DNF (Bool Bool Bool Bool) Bool)
(assert (= (DNF p1 p2 p3 p4)
           (or
		(and p1 p2 p3 p4)
		(and p1 p2 (not p3) (not p4))
		(and p1 (not p2) p3 (not p4))
		(and p1 (not p2) (not p3) p4)
		(and (not p1) p2 p3 (not p4))
		(and (not p1) p2 (not p3) p4)
		(and (not p1) (not p2) p3 p4)
		(and (not p1) (not p2) (not p3) (not p4)))
	   )
	)

; Now we show that these functions are two by two equivalent
; To do that, we use our already defined lrarrow2 function
; wff's A and B are equivalent iff (A <-> B) is a tautology
; Which means, !(A<->B) should be UNSAT.





(assert (not (and (=> (CNF p1 p2 p3 p4) (DNF p1 p2 p3 p4)) (=> (DNF p1 p2 p3 p4) (CNF p1 p2 p3 p4)))))
(check-sat)
;(get-model)

(assert (not (and (=> (CNF p1 p2 p3 p4) (BICON p1 p2 p3 p4)) (=> (BICON p1 p2 p3 p4) (CNF p1 p2 p3 p4)))))
(check-sat)

(assert (not (and (=> (BICON p1 p2 p3 p4) (DNF p1 p2 p3 p4)) (=> (DNF p1 p2 p3 p4) (BICON p1 p2 p3 p4)))))
(check-sat)
