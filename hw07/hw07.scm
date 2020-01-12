; COMPLETED ALL OK :D !!! 31/12/19

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
   ((= n 1) b)
   ((even? n) (pow (square b) (/ n 2)))
   ((odd? n) (* b
                (pow (square b)
                     (/ (- n 1) 2)))))
)

(define (ordered? s)
  (define (nexth x)
          (cond
            ((null? (car x)) (= 1 1))
            ((null? (cdr x)) (= 1 1))
            ((< (car (cdr x)) (car x)) (= 1 0))
            (else (nexth (cdr x)))))
  (nexth s)
)

(define (empty? s) (null? s))

(define (add s v)
    (cond
      ((empty? (car s)) (cons v nil))
      ((< v (car s)) (cons v s))
      ((= v (car s)) s)
      ((> v (car s)) (if (empty? (cdr s))
                         (cons (car s) (list v))
                         (cons (car s) (add (cdr s) v)))))
    )

; Sets as sorted lists
(define (contains? s v)
    (cond
      ((empty? s) (= 1 0))
      ((> v (car s)) (contains? (cdr s) v))
      ((= v (car s)) (= 1 1))
      ((< v (car s)) (= 1 0)))
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
    (cond
      ((empty? s) ())
      ((empty? t) ())
      ((contains? s (car t)) (cons (car t)
                                   (intersect s (cdr t))))
      (else (intersect s (cdr t))))
    )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond
      ((empty? t) s)
      ((contains? s (car t)) (union s (cdr t)))
      (else (union (add s (car t)) (cdr t))))
    )

; COMPLETED ALL OK :D !!!


