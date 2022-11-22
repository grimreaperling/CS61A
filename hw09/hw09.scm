(define-macro (when condition exprs)
  (list 'if condition (cons 'begin exprs) (list 'print ''okay))) 

(define-macro (switch expr cases)
  (cons 'cond
        (map (lambda (case)
                        (cons `(equal? (quote ,(car case)), expr) (cdr case)))
             cases)))
