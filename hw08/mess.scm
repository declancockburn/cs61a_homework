(define (only-greater x y)
        (if (< x y)
            (define x y) ;(define x y))
            ())
        (< x y)
        )

(define a 2)
(only-greater a 3)


(define (test1 x)
  (define (test2 y) (> x y))

(filter (greater-than-y 3 1) '(1 2 3 4 5)))

(define (not-lower x) (> x (car lst)))

(define (not-lower lst)
  (filter (lambda (x) (> x (car lst))) lst))
(not-lower '(3 4 1 2 3 5))
