; Write a function that returns the factorial of a number.
(define (factorial x)
  (cond
    ((or (= x 0) (= x 1)) 1)
    (else (* x (factorial (- x 1))))))

(factorial 4)


; Write a function that returns the nth Fibonacci number.
(define (fib n)
  (cond
    ((= n 0) 0)
    ((= n 1) 1)
    (else (+ (fib (- n 1)) (fib (- n 2))))))

(fib 5)


; Write a function which takes two lists and concatenates them.
; Notice that simply calling (cons a b) would not work because it will create a deep list.
(define (concat a b)
  (if (null? a)
      b
      (cons (car a) (concat (cdr a) b))))

; scm> (concat '(1 2 3) '(2 3 4))
;(1 2 3 2 3 4)


; Write a function that takes an element x and a non-negative integer n, and returns
; a list with x repeated n times.
(define (replicate x n)
  (cond
    ((= n 0) ())
    ((= n 1) (list x))
    (else (cons x (replicate x (- n 1))))))


; scm> (replicate 5 3)
; (5 5 5)