; Boolean majority function over three
; variables {x,y,z}

(echo "Hello Z3 world!")

(declare-const  x Bool)
(declare-const  y Bool)
(declare-const  z Bool)

(declare-fun phi (Bool Bool Bool) Bool)
(assert (= (phi x y z)
	   (or (and x y)(or (and x z)(and y z)))
	)
)

(declare-fun psi (Bool Bool Bool) Bool)
(assert (= (psi x y z)
	   (and (or x y)(and(or x z)(or y z)))
	)
)

;(assert (= (phi x y z) (psi x y z)))
(assert (not (= (phi x y z) (psi x y z))))

(check-sat)
(get-model)