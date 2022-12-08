(define (make-long-or args)
    (if (null? args) #f
        `(let ((v1 (eval ,(car args))))
        (if v1 v1 ,(make-long-or (cdr args))))
    )
)

(expect (eval (make-long-or '((= 1 0) #f (+ 1 2) (print 'goodbye)))) 3)
(expect (eval (make-long-or '((> 3 1)))) #t)
(expect (eval (make-long-or '())) #f)