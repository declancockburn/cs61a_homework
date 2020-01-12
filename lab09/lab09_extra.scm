;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7

(define (filter f lst)
  (cond
   ((null? lst) nil)
   ((f (car lst)) (cons (car lst) (filter f (cdr lst))))
   (else (filter f (cdr lst))))
)


(define (remove item lst)
  (filter (lambda (x) (not (= item x)))
          lst))


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
  (filter (lambda (x) (not (= (car s) x))) lst)
)

; Q9
(define (substitute s old new)
  (cond
   ((null? s) nil)
   ((pair? (car s)) (cons (substitute (car s) old new)
                          (substitute (cdr s) old new)))
   ((eq? (car s) old) (cons new (substitute (cdr s) old new)))
   (else (cons (car s) (substitute (cdr s) old new)))))

; Q10
(define (sub-all s olds news)
  (cond
    ((null? olds) nil)
    ((null? (cdr olds)) (substitute s (car olds) (car news)))
    (else (sub-all (substitute s (car olds) (car news))
                   (cdr olds)
                   (cdr news)))))
