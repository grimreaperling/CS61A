(define (nondecreaselist s)

    (if (null? (cdr s))
        (cons s nil)
        (let ((rest (nondecreaselist (cdr s))))
            (if (> (car s) (car (car rest)))
                (cons (cons (car s) nil) rest)
                (cons (cons (car s) (car rest)) (cdr rest))
            )
        )
    )
)

(expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

(expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
        ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))