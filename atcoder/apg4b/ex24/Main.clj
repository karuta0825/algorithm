(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(defn compute-second
  [h m s]
  (+ (* h 60 60) (* m 60) s))


(defn get-time
  [i]
  (let [s (if (neg? i) (+ (compute-second 24 0 0) i) i)
        second (mod s 60)
        minute (mod (quot s 60) 60)
        hour (mod (quot (quot s 60) 60) 24)]
    (list hour minute second)))


(defn time-format
  [time]
  (if (< time 10)
    (str "0" time)
    (str time)))


(let [input (create-input (read-line))
      diff (Integer/parseInt (read-line))]
  (->> input
       (map time-format)
       (join ":")
       println)

  (->> input
       (apply compute-second)
       (+ diff)
       get-time
       (map time-format)
       (join ":")
       println))
