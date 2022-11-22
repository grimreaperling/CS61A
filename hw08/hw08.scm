(define (my-filter pred s)
  (if (null? s)
      nil
      (if (pred (car s))
          (cons (car s) (my-filter pred (cdr s)))
          (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
  (helper lst1 lst2 0))

(define (helper lst1 lst2 flag)
  (cond 
    ((and (null? lst1) (null? lst2))
     nil)
    ((null? lst1)
     lst2)
    ((null? lst2)
     lst1)
    ((equal? flag 1)
     (cons (car lst2) (helper lst1 (cdr lst2) 0)))
    ((equal? flag 0)
     (cons (car lst1) (helper (cdr lst1) lst2 1)))))

(define (accumulate joiner start n term)
  (if (equal? n 0)
      start
      (joiner (term n)
              (accumulate joiner start (- n 1) term))))

(define (no-repeats lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (no-repeats
             (my-filter (lambda (x) (not (= x (car lst))))
                        (cdr lst))))))
