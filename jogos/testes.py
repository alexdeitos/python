import collections
numeros = [23,48,59,28,40,9, 54,6,46,21,59,34, 26,20,19,51,52,57, 5,60,18,39,35,30, 28,18,20,6,2,3, 13,53,16,36,55,54, 60,46,12,6,32,31, 24,55,46,16,11,54, 7,46,28,30,44,1, 58,39,27,7,24,12, 44,1,31,53,46,58, 31,20,47,43,2,11, 47,59,14,56,50,15, 27,21,3,11,15,49, 37,8,17,29,10,40, 38,41,20,24,25,13, 42,49,26,31,19,21, 41,11,12,46,20,40, 28,43,4,29,52,30, 21,19,1,9,34,54, 19,40,35,44,27,4, 35,17,30,25,42,57, 11,21,46,14,25,50, 17,46,43,53,52,39, 54,41,1,46,58,44, 25,33,10,12,18,5, 4,16,44,49,12,34, 44,59,29,19,41,22, 50,44,60,38,56,8, 27,3,39,40,36,43, 16,46,13,11,24,31, 12,45,10,56,2,27, 13,40,50,46,3,44, 6,4,17,57,34,51, 58,56,18,8,2,37, 1,35,13,11,10,49, 30,15,5,58,20,27, 2,38,27,60,18,8, 51,28,24,49,9,45, 11,51,6,24,13,19, 49,29,56,43,35,16, 4,33,16,44,19,31, 54,34,52,8,14,27, 13,17,27,11,15,22, 12,11,10,59,38,37, 11,8,18,40,37,51, 38,48,5,49,10,32, 24,3,27,38,14,56, 19,18,53,34,2,23, 4,53,35,43,47,46, 25,49,12,21,38,37, 20,37,26,7,39,38, 56,33,1,19,18,60, 25,33,42,49,6,48, 40,42,13,18,35,41, 58,55,46,22,40,10, 55,37,58,14,2,1, 30,36,2,11,39,15, 37,13,16,26,39,35, 6,15,43,5,12,22, 7,9,23,33,57,59, 42,8,18,37,58,23, 55,12,15,30,52,18, 22,13,10,20,12,54, 35,46,34,60,24,33, 5,26,42,27,48,34, 40,3,48,17,34,35, 5,47,40,9,42,3, 59,2,11,32,26,13, 27,55,35,6,25,45, 4,11,43,20,30,37, 55,53,14,10,36,60, 10,19,29,24,6,25, 8,15,34,25,10,23, 33,45,44,40,36,54, 11,39,41,9,25,8, 5,4,36,56,40,44, 19,4,23,29,59,56, 37,38,20,13,10,54, 29,47,22,36,34,18, 53,43,46,25,35,6, 39,4,7,12,26,22, 12,27,40,37,22,55, 57,50,56,51,58,59, 37,5,44,1,53,6, 33,50,38,32,8,31, 19,10,27,31,51,53, 10,39,38,35,26,19, 18,19,44,54,1,29, 27,11,6,28,46,3, 27,46,15,25,50,45, 14,7,60,54,47,56, 53,58,21,38,57,56, 33,32,22,29,35,14, 10,12,54,42,22,25, 56,58,54,6,41,9, 28,22,6,31,44,12, 26,35,40,25,6,38, 60,30,14,45,23,16, 23,58,8,19,27,7, 52,35,49,30,38,36, 7,56,22,13,6,17, 40,10,18,33,38,43, 19,39,20,53,14,6, 23,39,18,55,50,37, 38,4,58,40,27,59, 15,37,18,33,40,6, 7,42,58,36,24,11, 11,15,39,37,29,44, 51,33,23,52,31,10, 52,56,4,24,46,55, 29,16,20,35,47,23, 23,56,8,7,1,6, 28,60,52,45,4,48, 32,37,40,60,7,14, 2,46,57,60,48,36, 41,46,54,59,23,52, 55,11,27,22,25,59, 56,10,11,2,38,24, 11,17,48,18,4,21, 18,58,32,39,27,17, 46,32,16,56,40,53, 6,36,53,30,56,23, 11,51,36,8,35,27, 28,35,58,54,2,32, 18,56,8,34,39,10, 1,48,50,44,37,46, 27,22,58,33,59,42, 41,14,54,4,39,58, 20,9,1,14,54,25, 22,19,33,11,53,34, 45,35,1,23,5,14, 40,50,43,28,51,34, 59,46,28,38,4,30, 22,20,52,60,42,36, 6,37,34,10,3,17, 42,38,49,15,50,37, 57,21,24,52,25,8, 14,7,35,1,31,46, 56,21,20,7,40,24, 14,37,39,26,35,29, 44,5,32,2,12,40, 50,57,48,17,6,33, 21,11,13,53,54,5, 19,34,44,36,20,28, 37,26,11,24,59,34, 40,58,30,32,15,22, 5,39,10,54,46,42, 10,58,14,45,31,34, 55,23,44,43,36,56, 9,36,29,28,34,55, 43,32,21,50,35,29, 14,22,6,5,10,36, 46,24,20,4,50,14, 15,6,39,19,37,53, 18,16,12,34,37,17, 38,23,45,32,29,22, 6,2,57,22,55,44, 28,3,32,34,37,16, 52,14,19,12,59,25, 8,24,47,26,11,57, 19,57,38,54,4,27, 17,16,60,12,52,1, 20,9,59,54,16,57, 54,10,52,41,44,4, 10,18,24,5,39,52, 30,59,20,32,8,48, 35,48,44,39,36,52, 32,39,13,54,30,46, 19,10,32,60,13,40, 28,26,55,38,48,35, 32,27,48,36,2,50, 34,60,5,4,7,42, 39,5,6,53,15,25, 50,30,25,17,32,26, 43,39,18,25,37,1, 56,43,21,8,27,35, 55,34,22,20,24,15, 23,47,29,2,14,22, 20,40,28,5,8,45, 15,41,45,33,36,27, 40,9,49,25,35,33, 45,29,42,9,43,26, 9,21,53,36,52,38, 55,14,16,21,33,19, 32,21,10,48,34,57, 30,1,14,56,22,6, 28,33,20,24,57,12, 52,59,55,40,8,33, 6,39,4,44,52,60, 8,54,21,10,45,4, 8,57,47,39,9,59, 43,11,39,9,30,12, 48,20,43,18,6,24, 38,1,9,48,49,24, 36,16,9,47,13,17, 39,29,24,52,7,45, 10,54,42,16,40,32, 10,29,24,43,6,55, 51,40,52,24,12,3, 24,17,10,1,3,23, 56,39,35,8,23,59, 15,19,35,59,14,2, 55,21,16,44,29,10, 34,8,2,15,9,22, 17,56,37,52,18,4, 10,52,23,36,3,43, 28,51,59,26,53,10, 11,5,30,31,13,19, 46,3,2,30,14,20, 47,43,38,1,17,45, 16,52,53,58,30,12, 46,34,59,45,9,42, 20,41,22,36,43,38, 19,10,16,15,28,35, 39,45,31,25,43,33, 60,28,54,37,45,11, 22,17,50,38,20,16, 4,36,25,21,46,33, 3,50,18,23,9,52, 57,21,2,33,20,48, 39,33,29,16,44,42, 14,56,52,17,4,43, 42,10,33,36,13,35, 32,16,33,23,18,30, 9,6,39,15,22,48, 47,43,45,40,57,11, 10,27,57,13,23,4, 3,48,44,35,25,38, 27,40,33,6,39,60, 43,54,29,57,35,56, 21,18,56,15,51,12, 9,43,10,15,45,28, 25,18,2,21,9,7, 30,53,26,11,37,12, 46,11,8,43,28,27, 48,35,44,23,36,20, 53,12,58,55,34,45, 52,9,58,47,22,25, 25,6,14,21,3,15, 3,5,2,34,10,15, 31,35,57,54,21,53, 17,58,45,19,28,16, 50,22,6,37,30,17, 47,1,3,19,23,58, 5,24,51,22,11,53, 30,25,23,44,28,16, 48,1,18,45,17,10, 23,56,41,46,34,11, 7,40,54,15,3,45, 59,7,18,23,32,14, 38,1,32,4,23,59, 28,59,16,47,27,60, 41,35,37,10,19,9, 30,10,53,44,3,56, 19,51,56,16,5,37, 20,58,10,59,57,5, 56,26,40,16,57,12, 35,13,32,16,24,23, 7,18,51,41,44,39, 53,45,47,1,52,55, 43,28,10,37,47,44, 25,5,53,28,41,54, 39,11,56,46,13,25, 17,58,33,52,11,3, 30,40,33,18,20,32, 11,26,24,52,40,23, 25,5,31,1,28,23, 3,43,21,17,22,10, 14,36,60,38,17,44, 42,5,32,37,1,31, 5,4,37,40,60,14, 23,45,16,58,59,56, 8,49,35,42,56,2, 45,9,60,2,35,4, 10,40,30,44,36,60, 13,26,1,21,14,51, 55,30,28,59,33,22, 53,35,52,25,23,13, 14,9,2,32,22,37, 6,38,24,39,15,10, 59,30,43,31,34,25, 2,41,39,1,34,45, 29,13,49,50,45,17, 35,22,8,37,21,18, 24,32,23,40,41,38, 35,27,3,11,44,5, 58,41,50,40,9,55, 45,1,57,49,50,6, 49,26,30,34,24,6, 9,3,29,13,30,51, 4,3,37,39,48,50, 28,26,33,41,8,54, 18,43,22,24,16,34, 6,51,13,38,49,3, 33,41,48,15,17,47, 28,32,22,56,58,7, 59,24,30,8,57,5, 41,48,57,50,44,54, 59,18,45,60,8,15, 50,36,8,28,47,58, 2,22,51,24,48,17, 2,42,3,27,16,7, 34,47,57,56,14,46, 55,15,48,32,28,27, 29,3,54,7,37,60, 53,32,30,7,24,13, 40,32,11,6,59,48, 43,33,53,26,54,42, 43,48,32,19,17,51, 21,54,10,50,51,11, 19,30,60,12,6,5, 54,34,59,21,9,4, 22,53,26,1,43,50, 53,31,19,52,36,22, 27,19,23,3,45,40, 37,26,18,30,33,17, 10,53,15,2,6,56, 47,1,26,55,39,4, 12,10,46,28,22,5, 60,8,25,39,41,11, 53,51,27,11,46,9, 51,9,13,15,19,11, 45,34,23,20,37,32, 32,37,5,35,17,57, 56,10,43,50,1,25, 23,12,54,46,9,24, 20,25,45,2,41,14, 43,15,22,1,16,25, 11,42,55,58,35,20, 17,49,27,22,57,31, 20,50,48,59,28,21, 4,29,8,49,38,50, 6,14,2,17,44,13, 19,45,43,6,54,34, 31,56,16,6,11,19, 53,1,3,4,51,39, 9,28,45,2,23,53, 2,57,35,13,54,14, 54,22,48,34,23,53, 55,50,42,58,47,30, 1,5,37,60,34,40, 56,13,22,54,14,58, 47,41,18,17,2,16, 55,12,50,18,53,46, 28,13,11,26,50,27, 57,59,6,25,43,58, 42,45,56,13,3,59, 1,29,13,25,5,26, 34,8,2,21,25,6, 27,5,42,54,41,11, 30,15,54,55,26,4, 38,16,21,4,18,6, 34,57,47,18,6,52, 22,8,52,1,53,49, 20,6,33,22,31,34, 25,56,30,12,39,57, 4,38,48,10,45,40, 55,4,44,38,19,52, 39,11,48,14,19,10, 31,2,51,42,18,56, 1,52,30,60,20,12, 45,41,39,30,15,59, 27,39,19,41,12,45, 38,2,27,28,32,20, 34,30,41,11,27,26, 32,44,54,60,47,37, 35,11,7,50,34,5, 44,26,39,35,16,45, 60,23,22,46,53,41, 1,28,56,37,6,58, 6,7,41,39,29,55, 21,9,15,36,12,31, 45,59,42,55,32,26, 53,36,10,9,50,55, 25,10,24,47,48,36, 2,14,21,60,22,51, 6,23,16,11,42,36, 43,13,28,56,37,25, 28,13,6,14,45,35, 48,5,30,18,8,2, 20,31,40,30,27,53, 54,8,45,29,35,15, 36,53,55,37,60,9, 42,22,51,23,57,15, 17,41,48,15,20,31, 33,13,14,3,43,29, 2,53,13,49,10,41, 53,34,59,33,48,6, 37,40,6,58,41,18, 13,47,60,18,52,9, 12,9,56,29,14,42, 34,31,29,4,10,35, 23,27,21,19,52,11, 49,18,20,32,15,48, 38,15,47,25,10,53, 34,17,9,46,10,32, 53,46,28,48,37,12, 59,5,51,42,50,8, 13,32,12,41,24,29, 46,16,33,45,34,6, 52,29,17,41,12,25, 5,9,41,14,3,46, 25,60,34,53,45,38, 59,49,43,5,27,18, 1,24,10,17,42,51, 53,14,44,7,23,43, 28,39,8,59,42,3, 4,6,41,40,19,20, 42,54,57,3,49,10, 26,31,30,18,16,34, 27,39,37,58,60,33, 27,60,30,14,46,52, 41,39,9,49,23,58, 12,33,4,38,36,19, 49,39,18,31,57,23, 44,22,31,54,34,1, 30,53,4,31,47,32, 9,58,16,44,2,37, 25,36,2,53,42,41, 20,16,35,40,60,53, 51,2,24,52,36,8, 3,29,10,16,23,27, 50,19,59,2,29,12, 38,22,50,45,26,39, 59,56,7,28,21,58, 30,7,47,35,19,42, 38,50,29,45,17,32, 36,27,20,7,16,52, 12,31,34,48,36,56, 50,37,51,27,29,25, 11,7,59,51,32,1, 49,3,35,39,23,26, 39,52,17,35,19,33, 9,3,18,40,32,56, 58,41,48,50,15,18, 1,10,30,33,38,6, 24,44,28,13,45,11, 8,30,23,51,53,58, 12,1,31,37,17,46, 36,43,38,24,58,44, 34,29,20,37,57,45, 19,18,38,5,21,15, 44,56,13,14,27,11, 39,45,58,10,1,24, 24,45,53,35,26,21, 41,2,53,5,13,27, 18,23,42,56,32,30, 15,58,24,37,46,49, 44,37,9,55,14,46, 39,46,18,51,31,3, 9,12,31,50,18,39, 48,4,12,34,32,33, 13,39,51,37,35,7, 1,33,8,11,6,50, 37,46,47,51,23,38, 28,2,1,46,27,47, 35,52,17,19,9,11, 52,33,15,28,51,10, 2,1,37,51,48,11, 36,3,35,56,18,34, 42,59,30,58,50,22, 35,10,47,5,24,23, 20,10,1,5,42,3, 21,31,56,55,45,27, 1,33,30,17,47,19, 29,28,31,48,45,49, 47,40,55,57,52,5, 51,24,56,7,12,44, 51,27,1,23,45,2, 20,11,16,1,56,5, 48,8,21,36,23,29, 20,27,49,40,55,18, 57,10,25,14,33,29, 16,48,43,27,58,13, 17,38,42,51,34,8, 20,33,37,49,4,10, 7,40,19,49,11,23, 10,54,37,45,14,7, 6,4,43,54,56,11, 56,46,7,24,28,53, 50,33,42,7,58,16, 45,22,27,21,1,32, 44,28,24,57,7,26, 27,44,8,35,38,41, 23,57,29,17,60,38, 54,33,24,44,38,42, 48,18,15,22,20,16, 38,54,23,12,17,53, 34,23,41,19,40,58, 31,37,21,38,8,18, 10,16,34,13,60,22, 19,20,16,60,28,37, 47,3,43,42,60,23, 51,30,29,33,46,23, 6,18,46,23,31,2, 35,51,34,49,16,29, 38,2,42,58,41,1, 5,56,24,55,1,47, 33,19,52,51,35,26, 30,32,51,8,28,23, 44,9,33,10,23,51, 2,11,49,13,36,1, 18,56,27,6,24,59, 47,48,44,60,4,29, 30,43,7,44,1,54, 47,20,35,4,59,24, 38,26,60,34,29,50, 26,57,20,32,45,41, 3,52,5,43,35,14, 45,11,22,52,36,40, 32,2,27,47,58,41, 33,56,59,43,50,49, 21,7,5,53,45,4, 24,22,38,49,10,39, 57,23,38,13,34,27, 46,17,5,42,47,8, 9,51,20,24,52,43, 23,31,47,54,3,26, 46,40,58,31,28,42, 26,20,5,44,33,31, 49,27,43,17,14,21, 31,18,4,46,44,49, 17,51,36,6,42,13, 24,51,50,28,58,47, 36,53,35,9,1,4, 2,26,6,13,53,60, 6,43,17,5,54,59, 32,41,51,7,31,52, 54,1,15,37,46,42, 42,30,9,19,31,21, 21,40,51,27,24,2, 13,53,20,31,60,27, 8,44,40,35,22,12, 60,24,56,45,10,8, 9,46,23,32,35,57, 35,10,15,58,36,3, 36,47,42,29,53,31, 16,52,5,44,10,50, 5,12,1,7,45,10, 59,5,42,8,46,2, 53,43,23,6,7,8, 4,17,38,9,18,21, 41,49,36,42,31,38, 4,23,55,10,38,33, 40,7,44,55,34,20, 11,41,51,5,19,4, 36,29,23,49,32,45, 8,21,19,30,52,56, 47,58,8,43,39,46, 55,47,43,48,49,2, 27,54,28,50,22,3, 18,2,9,47,17,45, 4,17,1,48,13,38, 31,34,15,14,25,30, 1,6,14,17,33,36, 34,25,40,51,60,49, 6,53,56,30,37,3, 25,32,11,59,51,14, 26,30,21,15,13,46, 1,5,4,45,14,56, 6,28,33,48,46,27, 7,16,36,35,38,21, 46,42,27,45,20,47, 46,60,55,32,3,29, 18,46,42,15,56,24, 42,15,18,31,5,53, 28,58,19,24,42,25, 53,38,30,2,15,48, 11,32,60,5,6,36, 43,41,37,51,18,39, 54,44,38,25,46,53, 43,36,1,20,13,6, 12,10,51,37,23,47, 28,26,54,55,23,60, 30,47,53,38,20,36, 37,58,12,29,8,16, 31,42,15,7,17,54, 46,18,16,45,31,4, 7,52,11,10,1,4, 5,52,59,2,33,23, 30,52,50,49,53,32, 29,21,20,46,22,60, 7,18,26,46,39,24, 2,23,38,15,21,19, 21,56,36,9,13,27, 32,53,16,20,12,10, 44,41,42,54,47,19, 28,21,9,10,2,18, 38,44,17,60,4,53, 6,48,11,45,4,24, 30,50,45,2,35,21, 30,7,23,20,15,41, 7,12,57,11,30,39, 37,5,24,44,49,58, 54,47,27,17,3,32, 10,49,8,58,20,26, 35,52,27,53,57,23, 6,56,33,50,51,10, 18,32,29,13,50,58, 55,25,9,8,54,41, 28,12,34,29,1,48, 29,21,47,57,13,34, 42,2,11,23,31,44, 24,41,12,42,44,13, 53,10,28,16,48,33, 35,17,15,34,49,11, 4,13,58,36,19,15, 32,44,42,48,16,36, 51,47,28,10,59,16, 30,46,35,54,26,2, 40,53,12,46,2,52, 25,39,44,41,31,22, 33,5,23,32,8,56, 18,30,14,11,33,39, 36,46,48,31,7,35, 6,23,56,15,5,59, 28,8,55,41,48,9, 45,38,52,17,7,56, 34,60,18,45,4,20, 59,49,13,18,4,14, 23,16,17,59,42,60, 31,57,17,56,28,58, 35,11,28,46,42,58, 8,29,31,4,17,45, 1,8,44,17,46,53, 27,51,1,46,59,6, 58,39,18,17,35,30, 46,24,51,50,56,52, 49,34,42,18,3,14, 32,1,6,9,16,2, 41,2,42,30,12,10, 36,22,42,3,16,4, 6,43,22,52,57,51, 13,37,54,7,29,1, 57,43,18,59,10,31, 26,37,8,22,54,33, 11,46,27,49,6,40, 58,7,27,45,4,5, 28,18,41,54,14,47, 13,49,4,44,14,57, 50,28,35,24,2,14, 30,24,12,49,7,27, 48,44,46,4,18,9, 56,6,45,60,26,50, 31,32,43,3,52,1, 48,15,24,28,1,26, 4,51,45,22,38,25, 4,17,23,28,9,53, 10,1,34,54,6,40, 30,59,27,36,4,54, 49,29,17,53,20,24, 55,53,1,35,56,39, 11,9,6,34,41,53, 40,27,55,17,28,44, 9,14,26,36,52,21, 57,21,54,48,50,60, 10,40,27,47,55,37, 50,59,56,46,3,4, 26,10,4,37,47,57, 13,12,51,37,48,44, 2,43,11,1,3,28, 60,12,57,58,33,2, 12,23,25,18,45,50, 58,33,36,40,25,10, 2,34,51,36,38,55, 4,56,54,13,35,58, 2,20,37,19,1,10, 41,53,26,23,52,24, 4,13,51,37,6,34, 11,6,53,44,16,26, 59,2,54,32,24,50, 40,22,13,29,48,28, 5,9,25,40,38,27, 44,31,49,54,36,47, 50,52,14,4,27,38, 2,6,35,30,52,34, 2,16,4,44,33,51, 34,16,46,15,42,59, 36,6,40,14,8,26, 33,14,52,36,32,41, 27,52,41,29,4,48, 47,32,25,57,6,13, 50,57,58,28,2,14, 57,10,33,2,11,52, 27,45,44,26,38,31, 2,18,30,56,52,6, 25,29,36,1,56,60, 1,41,28,33,39,19, 13,32,6,51,40,24, 41,32,19,58,5,49, 2,5,55,28,27,48, 52,32,12,54,20,48, 12,20,13,49,34,30, 56,29,53,36,38,17, 6,28,56,2,36,51, 35,55,2,43,34,42, 49,7,33,31,36,14, 48,37,26,22,38,23, 1,23,13,30,24,57, 45,47,50,52,15,4, 3,34,58,22,18,55, 14,46,40,13,4,52, 16,24,25,45,59,42, 33,54,40,5,9,13, 19,2,30,46,22,52, 9,22,60,48,12,39, 15,55,37,34,19,7, 47,44,53,56,8,39, 24,44,6,15,18,30, 7,29,50,16,38,36, 60,38,29,3,7,15, 43,8,21,27,3,25, 17,44,2,5,13,39, 31,39,59,19,53,44, 45,16,18,11,36,2, 52,21,48,58,30,17, 7,8,10,27,12,56, 12,56,5,52,45,59, 49,3,19,35,22,24, 51,49,46,40,36,26, 44,49,57,37,21,46, 54,33,13,55,45,15, 6,8,37,24,45,41, 32,44,12,8,48,46, 54,29,18,42,40,50, 50,6,47,58,26,19, 43,39,20,19,24,4, 53,42,31,43,29,18, 7,10,38,17,24,57, 14,17,32,37,39,3, 7,32,31,51,27,8, 16,39,13,26,42,20, 38,10,27,2,21,9, 12,11,54,33,48,25, 34,26,9,43,54,53, 39,43,60,57,34,56, 42,51,14,40,32,33, 15,56,3,27,4,7, 52,48,54,58,55,29, 5,44,11,19,17,48, 11,35,16,46,24,50, 44,28,18,24,4,39, 43,8,2,28,33,12, 19,7,12,34,53,40, 29,27,19,4,28,31, 1,44,39,16,57,28, 54,31,50,43,29,22, 43,27,18,52,50,32, 39,56,28,12,51,38, 42,37,35,27,59,36, 56,18,31,2,30,45, 9,55,23,44,7,46, 17,27,55,13,5,16, 44,30,27,11,40,57, 52,14,3,60,57,55, 45,5,36,12,50,58, 18,17,59,2,54,5, 25,5,13,12,35,2, 53,49,21,11,54,9, 25,28,53,45,14,58, 21,33,28,31,43,6, 52,39,7,27,55,57, 46,60,58,36,40,3, 47,11,8,49,3,4, 2,27,59,49,4,5, 32,24,16,38,5,46, 10,26,29,38,32,21, 38,29,43,13,7,2, 59,44,54,37,27,12, 50,35,32,26,2,24, 20,13,40,10,53,44, 52,25,42,45,35,57, 58,19,12,22,2,36, 37,27,44,30,38,23, 50,25,17,16,54,2, 12,17,28,53,6,10, 16,15,37,3,35,47, 55,52,26,19,1,24, 21,46,6,22,13,31, 39,49,11,24,17,46, 2,42,8,49,48,38, 47,11,3,27,32,13, 35,59,36,9,18,24, 13,50,41,36,56,33, 4,36,29,55,45,3, 9,19,20,50,60,51, 38,45,39,7,12,56, 19,45,54,56,46,9, 59,47,32,48,40,12, 50,40,26,7,19,17, 19,42,8,36,21,59, 51,31,42,20,56,19, 5,60,46,42,50,7, 11,40,37,20,1,52, 36,21,13,59,60,30, 59,10,16,14,7,54, 19,33,18,43,60,1, 38,2,45,35,20,51, 51,54,32,1,38,47, 49,3,51,20,22,14, 8,25,27,6,10,1, 25,51,26,42,28,33, 5,13,3,24,35,59, 24,46,39,57,26,9, 48,8,21,18,49,30, 43,50,8,7,39,11, 43,27,59,53,23,10, 41,35,36,16,52,54, 30,19,10,18,50,11, 35,2,20,43,5,16, 29,44,51,31,18,57, 25,37,15,6,48,55, 55,43,21,10,47,53, 51,59,47,10,60,53, 38,17,55,41,24,25, 16,4,18,27,5,51, 34,46,14,28,11,16, 35,29,37,13,6,30, 48,34,25,42,13,8, 27,29,1,50,52,38, 42,44,52,58,60,38, 39,26,49,1,4,43, 28,30,29,22,20,5, 54,7,19,12,45,9, 14,8,53,9,59,32, 7,12,25,26,32,39, 24,33,7,30,47,8, 10,47,54,7,43,32, 45,6,19,34,43,22, 44,11,5,46,36,3, 35,23,15,7,20,14, 19,51,54,8,52,46, 44,15,56,2,10,57, 16,25,3,51,23,56, 46,43,59,54,44,53, 56,32,8,22,43,53, 60,14,53,30,15,55, 2,56,11,5,59,13, 49,43,14,10,53,46, 20,2,43,15,5,57, 6,50,4,48,29,51, 24,50,1,44,13,40, 30,31,23,9,54,11, 18,57,58,40,47,54, 14,50,3,23,2,34, 13,8,27,1,3,52, 42,32,56,40,30,17, 33,42,12,31,11,52, 5,52,2,33,51,28, 33,10,15,38,31,28, 26,21,20,36,31,29, 59,8,60,44,40,30, 4,39,56,23,52,55, 36,14,30,38,11,8, 29,6,54,10,20,16, 8,29,36,35,14,40, 4,16,24,56,25,30, 50,59,18,31,60,12, 9,40,5,22,36,11, 58,55,14,2,60,48, 13,59,21,17,40,39, 60,26,19,58,13,40, 28,27,13,35,26,52, 2,52,39,59,48,1, 31,33,24,5,42,9, 51,5,27,4,15,17, 17,53,60,44,16,3, 47,58,4,41,20,30, 39,6,42,10,60,33, 13,50,46,24,60,19, 56,17,37,51,4,36, 41,53,18,4,36,26, 11,39,9,5,8,7, 10,41,14,22,53,42, 19,23,31,53,29,41, 39,54,58,46,4,6, 47,26,11,57,59,55, 27,15,30,52,26,2, 26,38,33,35,53,43, 23,5,54,39,38,51, 9,29,18,7,14,39, 2,51,17,44,43,23, 35,2,51,14,49,39, 48,27,34,52,46,5, 59,1,2,40,51,24, 3,40,8,53,51,36, 20,33,58,34,57,60, 9,11,24,3,51,36, 59,10,37,57,40,43, 34,10,37,50,43,2, 45,8,34,15,2,25, 32,19,23,57,9,29, 54,45,51,11,34,48, 13,26,25,10,28,45, 22,42,49,8,12,9, 15,1,48,37,39,52, 40,45,24,14,13,39, 26,21,39,5,18,59, 17,20,38,8,53,3, 16,49,55,20,10,26, 3,5,24,19,30,35, 49,22,59,29,32,54, 12,18,15,8,11,22, 20,27,49,5,23,39, 37,35,12,22,19,9, 12,49,60,32,30,40, 36,10,60,52,50,23, 35,31,4,30,54,28, 31,55,56,50,40,10, 32,55,34,31,50,40, 41,19,57,53,21,27, 17,15,48,42,35,47, 26,19,48,57,5,8, 46,5,58,37,14,43, 48,55,52,43,5,15, 34,37,41,53,2,33, 33,23,29,46,10,31, 5,43,28,15,11,50, 7,25,4,58,13,27, 47,51,10,50,30,25, 5,41,29,36,30,48, 3,53,45,11,34,26, 35,50,2,23,33,40, 36,54,3,31,15,48, 3,7,9,10,31,34, 30,17,38,14,5,35, 45,12,1,26,54,20, 32,35,22,9,56,11, 2,11,37,36,48,6, 14,4,26,35,29,13, 10,25,5,39,52,43, 55,30,33,9,7,38, 9,60,11,53,48,8, 36,32,55,49,60,28, 10,3,39,54,56,11, 58,28,23,39,16,19, 29,22,36,58,41,48, 39,54,36,37,60,49, 60,3,20,19,58,6, 27,17,57,26,55,20, 24,53,41,6,13,50, 12,54,2,32,14,9, 49,17,20,59,57,52, 25,22,11,16,33,3, 11,53,56,37,10,19, 50,21,14,35,31,27, 60,52,59,9,44,20, 8,49,43,17,40,19, 41,12,15,7,13,8, 54,10,2,43,21,35, 4,23,27,28,9,30, 12,5,10,20,29,37, 52,29,56,60,2,4, 44,18,45,31,26,20, 60,12,34,30,44,57, 59,28,47,60,22,5, 1,53,22,50,45,30, 33,52,55,47,38,50, 21,11,49,14,33,30, 2,3,12,37,47,16, 7,52,6,51,47,39, 7,25,24,36,5,47, 28,52,6,43,12,56, 41,3,10,30,57,13, 46,11,27,34,49,13, 14,1,11,23,42,48, 47,20,4,56,53,5, 43,28,56,20,52,51, 35,28,54,30,22,31, 20,52,60,42,54,40, 17,6,14,40,49,26, 5,51,31,53,47,17, 31,25,18,41,22,30, 48,47,7,4,42,51, 40,5,3,48,1,18, 53,46,5,6,34,55, 23,31,60,55,30,54, 46,9,43,41,49,29, 31,49,44,24,9,48, 28,58,41,40,51,20, 4,14,21,26,12,28, 55,46,34,17,19,6, 47,36,44,29,20,14, 1,25,4,14,21,51, 28,17,35,52,31,15, 46,54,8,36,7,23, 48,32,29,55,27,28, 23,39,52,31,6,33, 10,34,53,33,28,6, 19,3,60,33,24,16, 19,10,49,18,1,44, 35,47,60,44,30,3, 28,31,15,58,3,26, 40,9,37,58,50,60, 49,58,40,46,10,27, 36,42,37,9,28,31, 4,25,18,15,36,2, 21,28,19,25,50,43, 7,31,32,37,43,34, 5,4,19,39,6,23, 29,36,56,22,9,51, 16,5,58,39,10,21, 52,30,27,12,55,33, 49,34,36,1,16,8, 23,49,32,54,18,5, 47,19,17,12,32,55, 60,8,39,52,24,16, 24,8,14,5,29,30, 59,31,57,4,52,42, 7,42,56,29,33,3, 49,11,7,18,16,33, 19,4,39,14,45,60, 49,44,56,26,46,55, 18,4,59,54,56,17, 50,55,7,35,44,40, 44,54,41,45,34,10, 55,44,8,20,43,21, 27,35,40,1,6,17, 17,20,4,47,9,13, 44,41,18,50,37,30, 16,3,22,54,25,15, 47,36,29,59,3,6, 4,34,52,32,58,43, 4,43,25,9,33,32, 26,45,6,28,42,14, 11,52,14,6,29,8, 60,44,7,39,43,9, 36,20,54,9,3,53, 4,15,50,60,43,47, 43,1,50,28,57,15, 3,35,58,49,2,6, 41,19,10,28,55,56, 46,23,9,35,11,51, 7,12,57,6,24,10, 41,33,17,18,7,42, 55,44,38,35,14,31, 30,20,21,11,50,52, 21,48,33,1,56,17, 3,41,52,14,13,16, 27,23,36,10,21,16, 10,9,48,36,41,21, 27,49,38,23,41,19, 40,30,1,9,33,34, 27,56,17,24,49,23, 24,9,40,20,36,42, 37,48,32,2,18,20, 24,42,35,31,6,57, 36,46,28,32,3,20, 45,4,6,23,10,2, 39,50,21,12,40,55, 20,5,29,59,40,33, 20,28,42,23,10,43, 4,40,50,17,55,38, 9,56,29,52,16,24, 56,11,20,41,34,18, 36,12,37,24,5,28, 3,6,45,34,41,43, 11,6,18,5,37,9, 32,33,10,19,42,4, 53,39,16,21,10,12, 3,47,10,50,29,23, 44,36,32,8,34,25, 19,18,54,47,43,9, 5,37,43,7,53,54, 41,53,8,23,5,16, 28,17,49,53,45,9, 44,48,25,57,27,47, 14,10,56,25,4,28, 10,43,49,32,25,6, 7,57,19,43,39,30, 28,4,19,16,49,29, 49,1,22,47,44,50, 55,8,2,37,23,33, 9,41,56,23,21,30, 1,41,3,18,16,42, 37,1,14,45,12,16, 20,51,57,45,24,18, 15,49,59,4,3,2, 38,8,50,53,59,6, 27,32,15,12,20,16, 41,27,13,60,14,18, 15,42,27,53,34,49, 8,11,16,15,57,52, 57,11,7,43,10,13, 60,14,45,24,33,26, 34,17,52,5,2,29, 57,3,38,21,28,16, 1,2,10,48,14,8, 57,40,28,42,54,55, 31,6,5,17,50,1, 58,10,39,11,13,35, 25,14,51,48,60,21, 25,46,51,18,13,30, 12,10,36,54,44,57, 44,1,28,55,6,39, 52,2,20,27,36,24, 51,7,6,28,35,43, 56,36,4,44,46,53, 27,39,36,10,41,52, 51,60,1,11,59,26, 20,42,1,3,49,18, 39,6,5,33,54,17, 57,43,15,29,26,16, 49,33,24,40,46,43, 57,8,54,1,23,37, 17,5,16,24,20,32, 54,26,34,51,20,52, 20,18,47,44,60,33, 10,33,51,53,6,17, 52,40,29,27,28,10, 28,53,18,39,22,29, 45,40,2,7,18,8, 31,21,40,39,56,5, 42,55,51,43,2,33, 19,32,52,1,2,39, 29,47,4,13,46,23, 55,51,58,9,44,24, 31,51,19,6,56,34, 11,9,25,5,60,20, 49,8,28,3,26,17, 60,57,9,25,8,41, 7,9,20,41,12,19, 47,19,58,14,40,55, 30,2,52,21,11,35, 2,46,3,37,13,54, 34,12,1,6,58,29, 7,15,42,48,34,13, 49,27,4,36,52,37, 48,17,4,33,55,2, 6,41,4,37,12,42, 45,47,29,40,44,43, 10,27,23,5,16,26, 3,31,7,25,40,58, 15,37,27,12,60,51, 49,58,53,39,38,29, 44,36,55,58,18,24, 28,21,4,32,3,22, 18,53,55,32,9,17, 21,23,20,7,29,15, 4,54,55,36,16,31, 44,40,58,29,3,20, 26,25,42,60,5,24, 6,8,4,1,25,28, 8,38,60,41,15,9, 29,18,2,15,10,39, 38,21,27,2,29,32, 48,17,46,56,60,8, 47,27,13,31,34,58, 32,6,31,24,15,19, 4,56,18,59,46,16, 46,20,4,43,47,10, 38,45,40,16,32,22, 12,24,8,40,43,49, 8,41,53,1,58,34, 35,17,59,15,36,29, 28,3,39,51,31,15, 42,58,12,18,16,27, 17,3,9,32,7,5, 28,53,38,23,14,25, 33,9,37,40,41,30, 45,20,38,31,16,12, 53,36,8,30,1,47, 33,18,15,56,31,34, 4,14,33,44,11,45, 57,34,5,54,28,21, 56,35,50,13,41,25, 30,4,13,60,51,1, 18,14,57,30,13,5, 1,58,26,28,4,41, 36,39,57,58,5,30, 42,13,33,20,8,26, 37,17,15,50,48,59, 2,48,49,40,55,11, 16,53,2,4,21,36, 34,6,33,18,53,19, 57,3,5,11,33,39, 13,22,7,33,51,48, 50,32,25,34,57,24, 46,51,47,59,54,57, 35,5,32,21,33,12, 8,5,24,18,57,33, 55,48,1,39,16,42, 54,11,27,18,2,30, 49,24,39,34,55,14, 48,59,49,41,42,23, 44,1,51,52,41,23, 22,44,41,46,52,54, 33,11,3,58,14,5, 59,1,47,5,52,12, 44,8,59,54,4,27, 16,58,43,37,52,59, 47,41,58,3,23,12, 5,52,18,8,59,42, 11,15,10,27,60,53, 25,33,51,31,5,37, 6,23,19,50,37,49, 35,15,27,57,50,59, 22,41,2,30,21,52, 5,33,14,29,44,22, 7,45,18,13,29,31, 25,48,44,3,21,1, 25,39,45,51,8,14, 2,21,42,53,36,17, 17,34,7,36,39,19, 46,20,55,37,28,49, 16,49,35,39,57,27, 32,10,49,60,4,33, 36,26,31,23,19,33, 40,41,34,33,21,59, 52,37,46,8,22,36, 51,27,60,21,20,2, 53,39,2,50,57,15, 41,49,45,19,13,12, 35,41,1,57,9,48, 17,57,55,24,52,5, 43,25,41,60,31,3, 38,44,8,4,12,52, 23,59,25,47,46,30, 33,37,5,38,28,36, 20,28,49,26,17,48, 33,51,9,23,45,12, 30,14,59,36,46,38, 26,21,54,4,19,29, 49,46,1,29,6,28, 53,29,36,3,15,27, 42,17,26,38,28,22, 19,1,9,25,50,52, 9,41,53,37,36,51, 35,39,29,24,7,14, 4,15,57,55,2,16, 32,44,59,53,48,51, 17,5,32,55,20,41, 52,55,23,50,58,18, 32,34,16,13,56,33, 4,21,59,18,38,34, 58,18,54,36,53,20, 4,8,3,54,45,30, 21,57,46,22,7,43, 31,11,41,35,22,5, 2,55,41,43,57,58, 37,24,44,28,20,41, 56,53,51,26,18,3, 1,49,52,42,19,44, 15,22,19,35,34,16, 9,21,22,7,17,54, 34,54,20,39,60,24, 50,24,40,54,52,60, 44,12,32,21,1,34, 50,55,37,33,59,17, 13,4,31,33,47,51, 22,11,2,14,39,12, 21,37,60,32,52,53, 42,45,44,60,41,17, 43,24,4,51,18,56, 51,30,49,25,37,46, 29,10,46,35,42,28, 37,12,43,38,11,54, 13,15,20,31,28,36, 4,12,41,45,60,8, 53,18,36,58,24,20, 59,20,52,42,44,10, 57,59,4,34,19,30, 18,55,58,43,31,5, 17,5,58,1,47,10, 52,8,43,34,40,21, 29,42,50,51,49,27, 57,51,21,22,25,40, 54,26,28,19,44,10, 36,48,27,40,5,46, 27,23,41,51,26,53, 31,11,33,42,57,8, 32,53,50,57,15,24, 19,35,12,2,11,8, 42,40,60,59,47,39, 22,8,17,42,44,2, 46,47,12,57,34,9, 31,37,54,23,4,18, 17,59,49,2,3,50, 11,40,41,47,15,42, 42,3,24,53,43,31, 17,3,24,27,44,25, 51,30,59,46,38,56, 14,38,6,23,44,34, 16,32,35,58,19,3, 60,22,59,25,44,7, 8,39,9,58,44,49, 56,34,17,32,47,27, 42,14,44,27,15,48, 47,54,2,50,3,44, 40,48,19,20,14,52, 54,24,44,57,34,16, 34,48,1,16,45,36, 51,44,60,9,7,30, 36,51,32,22,38,7, 43,29,35,59,31,17, 11,18,8,7,37,43, 9,30,47,38,23,44, 16,5,24,34,6,60, 28,22,38,17,52,59, 58,31,57,49,33,18, 44,10,17,16,51,34, 53,58,57,16,46,13, 17,49,15,33,39,23, 3,50,48,42,32,33, 53,51,2,41,13,49, 32,50,14,47,10,56, 23,50,53,42,28,38, 24,56,30,51,42,18, 45,6,8,7,53,27, 28,21,40,10,41,47, 33,48,6,7,20,9, 15,26,59,1,54,51, 4,17,41,10,27,52, 4,29,38,36,33,42, 17,45,32,21,10,46, 51,5,58,46,25,19, 44,41,22,8,9,25, 34,43,29,30,10,52, 21,47,40,52,30,20, 57,50,9,39,37,19, 11,2,46,50,8,41, 23,15,56,46,9,45, 57,39,54,11,38,13, 32,57,28,41,10,47, 4,33,1,48,5,37, 25,23,11,5,30,15, 15,21,31,46,2,57, 8,27,2,32,56,49, 60,41,47,26,35,18, 30,2,48,60,43,36, 13,59,37,56,3,47, 10,57,28,3,5,21, 14,24,60,6,18,48, 20,22,11,19,48,42, 1,7,56,11,37,38, 29,35,19,57,42,55, 32,9,4,52,29,3, 58,48,52,47,12,6, 19,24,43,34,39,5, 14,36,21,29,26,48, 56,47,55,38,42,3, 3,51,33,15,16,57, 43,56,9,45,29,34, 42,35,19,9,14,58, 22,2,19,28,43,6, 60,39,31,38,6,50, 31,57,17,19,29,44, 37,31,20,60,34,54, 27,31,26,11,10,41, 35,5,37,8,48,17, 42,56,8,37,27,53, 43,21,48,8,4,32, 11,23,59,42,35,2, 10,54,8,39,56,13, 10,50,28,51,59,7, 36,54,52,25,29,26, 45,20,36,37,31,51, 14,50,23,2,28,56, 57,35,60,41,3,15, 27,12,46,47,42,50, 37,5,54,58,46,10, 3,5,51,29,34,14, 38,51,52,60,10,35, 29,46,34,47,21,14, 4,34,25,35,48,12, 20,21,50,29,12,16, 33,37,59,30,4,8, 22,50,32,38,54,15, 1,50,19,42,24,58, 3,37,50,16,30,10, 7,3,55,47,53,45, 40,47,1,48,9,26, 39,9,21,12,37,54, 56,29,17,13,27,40, 12,17,60,44,46,45, 59,39,30,31,48,45, 47,59,1,23,36,43, 17,32,12,18,58,30, 37,50,41,5,38,27, 59,30,47,12,4,49, 4,42,34,50,3,13, 59,35,43,22,7,2, 25,4,29,42,24,23, 4,25,38,50,20,7, 58,17,54,10,42,33, 24,47,4,57,48,50, 1,7,19,51,35,2, 21,23,56,12,3,2, 49,12,10,57,25,1, 21,57,37,16,43,2, 26,46,12,23,39,4, 54,20,32,60,25,23, 34,17,7,41,2,50, 26,39,27,24,59,36, 29,47,12,50,16,28, 6,45,56,49,35,10, 15,30,14,42,26,54, 33,12,24,38,11,32, 1,21,38,41,56,49, 40,42,15,52,38,9, 44,45,27,29,43,54, 12,26,31,43,46,2, 49,19,53,50,17,6, 35,6,15,23,28,16, 45,15,2,54,16,50, 33,56,18,57,43,5, 44,42,13,8,24,32, 14,42,12,4,59,30, 40,47,1,5,7,37, 49,9,3,35,37,41, 34,51,55,17,48,27, 16,6,52,1,36,50, 60,36,57,18,44,9, 14,3,23,55,36,25, 12,56,44,51,31,54, 39,47,37,53,32,3, 7,35,21,39,58,33, 28,35,41,17,6,23, 29,2,7,50,16,32, 54,36,12,4,33,24, 17,53,39,8,7,35, 46,1,26,16,12,54, 35,7,53,58,8,43, 10,5,41,59,40,33, 46,25,5,49,39,34, 29,22,44,9,6,4, 45,13,39,47,9,7, 51,8,1,43,10,36, 22,10,17,7,2,60, 3,15,11,13,26,43, 2,27,50,34,18,4, 30,24,2,45,11,27, 1,56,18,58,45,57, 13,1,31,23,60,48, 2,3,24,40,31,14, 53,17,50,23,54,48, 22,8,27,43,55,12, 53,35,32,31,28,51, 37,16,34,57,53,9, 13,40,21,52,6,11, 15,19,29,53,37,41, 14,50,41,17,31,13, 33,18,60,11,58,57, 55,16,58,8,37,50, 15,41,8,47,12,53, 6,60,7,31,49,51, 47,30,52,11,21,35, 59,48,1,7,41,14, 33,5,4,54,15,26, 33,27,5,56,12,43, 50,37,33,40,19,17, 43,40,12,11,2,35, 60,37,47,36,4,27, 59,21,53,25,58,38, 44,2,26,5,3,22, 37,21,54,3,58,25, 44,46,31,14,40,42, 25,10,48,8,32,55, 49,32,15,9,41,42, 50,42,30,25,43,24, 22,32,18,29,42,38, 6,40,37,11,20,34, 43,34,53,38,28,24, 27,16,39,51,9,38, 42,59,58,37,48,22, 7,41,24,40,49,27, 49,33,56,2,14,1, 5,23,16,4,49,1, 7,26,16,29,45,55, 8,47,7,48,25,18, 12,1,55,59,38,36, 1,49,30,55,27,51, 4,60,56,25,18,23, 42,40,27,4,55,36, 53,5,38,54,46,11, 14,29,40,34,51,52, 41,20,36,3,11,6, 20,59,58,33,60,16, 59,37,46,36,35,51, 26,39,1,37,43,48, 10,11,56,40,41,6, 31,24,19,34,9,5, 24,18,57,56,10,20, 39,45,28,26,48,60, 53,59,25,29,10,24, 9,54,41,48,33,24, 5,48,23,42,45,29, 56,19,11,14,12,54, 13,47,60,32,49,10, 52,48,24,53,54,3, 57,29,31,27,34,14, 14,45,24,37,40,42, 51,17,56,36,44,40, 17,13,33,9,1,34, 12,42,59,46,19,60, 51,39,35,60,45,13, 42,10,50,41,11,36, 52,58,43,48,11,18, 30,32,34,50,28,26, 49,42,37,8,20,26, 13,41,24,42,10,56, 27,46,5,50,11,22, 2,54,48,51,19,28, 1,28,47,20,44,32, 16,53,20,60,12,45, 40,47,39,16,51,15, 8,16,22,56,58,30, 19,13,45,58,56,1, 49,8,22,18,7,39, 59,12,32,42,24,40, 39,23,34,52,8,43, 42,23,55,30,9,49, 59,27,19,29,50,38, 29,31,50,26,57,49, 22,1,29,13,32,3, 16,12,46,14,8,19, 60,10,3,8,24,13, 25,5,49,36,33,3, 24,16,26,54,12,2, 27,31,8,10,51,5, 60,31,12,48,57,16, 54,55,13,44,6,19, 55,33,15,50,53,18, 22,21,33,16,48,49, 25,49,30,43,47,45, 15,2,59,60,6,58, 30,6,37,19,24,13, 6,59,11,27,19,41, 41,6,23,55,32,35, 44,52,53,4,49,24, 41,49,51,25,15,46, 4,8,11,29,12,44, 38,60,13,7,55,46, 37,19,29,30,10,22, 18,39,54,34,31,16, 6,45,51,9,23,4, 5,16,53,38,50,34, 42,40,27,22,56,29, 43,60,28,11,54,14, 54,2,43,1,50,25, 10,53,55,29,13,47, 27,29,1,59,25,49, 55,14,59,47,13,42, 58,3,18,50,34,1, 25,51,5,18,4,28, 13,7,33,59,6,8, 45,13,46,55,53,11, 30,2,36,18,60,29, 45,38,13,11,54,39, 24,39,12,33,57,36, 30,53,23,7,32,8, 55,6,41,20,43,7, 13,40,29,59,45,51, 30,25,52,14,39,17, 38,16,18,28,15,47, 15,34,39,17,4,9, 48,3,58,18,56,23, 31,47,28,23,8,24, 18,43,52,39,7,8, 18,29,21,48,35,5, 32,23,2,10,44,17, 59,29,17,6,40,22, 33,3,20,60,9,16, 14,31,12,13,51,50, 35,32,36,33,51,15, 32,15,14,9,3,57, 25,41,17,29,13,22, 57,58,11,38,41,31, 17,6,20,18,13,37, 31,37,35,7,45,34, 38,13,32,20,10,49, 34,8,23,44,51,5, 37,35,23,16,57,55, 39,49,36,20,55,1, 32,18,11,30,2,58, 53,25,36,13,17,6, 59,57,7,58,31,14, 18,49,38,23,8,12, 8,45,30,33,17,10, 49,5,23,33,45,31, 47,29,31,15,60,42, 43,46,58,53,54,4, 22,54,52,47,49,9, 56,48,57,21,12,46, 17,56,16,38,39,45, 13,51,58,22,46,8, 51,49,14,47,59,58, 4,59,13,53,28,30, 46,4,54,17,13,5, 43,35,57,29,40,17, 11,33,56,47,17,34, 35,54,37,42,49,46, 49,4,19,28,35,6, 58,57,27,13,49,52, 22,4,30,44,28,49, 16,50,55,6,47,19, 45,43,56,25,52,3, 37,3,19,34,39,7, 14,22,25,15,37,23, 49,14,47,56,6,28, 48,57,23,8,31,3, 27,18,13,59,21,53, 13,4,12,53,9,52, 3,1,35,7,18,50, 32,21,25,1,6,49, 56,45,13,33,38,1, 34,28,37,12,8,31, 17,14,50,52,6,26, 3,59,21,36,55,31, 26,32,24,49,8,10, 47,29,34,48,19,41, 45,58,40,39,28,44, 49,52,15,25,14,6, 28,32,38,25,15,45, 32,34,17,35,9,12, 9,36,15,19,42,22, 44,8,5,15,18,10, 51,32,8,28,38,7, 24,5,34,13,35,33, 39,16,57,15,45,48, 15,52,40,36,51,42, 46,10,27,19,33,39, 8,40,58,4,53,31, 8,36,34,37,3,4, 30,45,58,1,4,41, 32,55,34,35,28,33, 46,56,5,15,45,10, 44,58,5,27,33,3, 31,37,34,15,38,4, 47,20,52,3,46,28, 39,19,11,8,50,30, 10,21,48,27,49,7, 50,7,33,21,24,13, 34,27,56,28,16,39, 35,21,54,29,38,36, 59,1,11,5,44,4, 49,28,2,6,57,50, 9,41,32,13,58,20, 41,20,19,29,59,10, 36,15,60,8,29,49, 28,32,49,53,18,20, 54,20,3,18,42,24, 57,2,15,6,56,18, 22,43,15,55,9,1, 5,11,29,54,23,58, 28,36,17,53,33,59, 30,39,35,43,15,57, 25,22,48,52,54,8, 50,42,19,8,30,14, 38,28,52,30,19,57, 53,19,38,18,17,49, 16,23,35,18,44,59, 13,56,12,33,53,54, 42,6,24,44,22,13, 36,38,33,14,49,41, 20,54,58,26,41,46, 30,8,31,3,21,25, 47,34,8,6,18,38, 38,43,20,55,17,58, 19,6,43,52,8,22, 34,3,12,50,32,40, 51,7,58,49,23,41, 12,3,38,29,51,4, 51,59,31,5,36,32, 51,58,23,11,8,37, 29,47,42,21,13,26, 23,6,25,39,51,5, 38,21,8,22,18,60, 28,16,45,29,30,11, 46,31,1,57,22,51, 6,33,45,38,24,50, 7,18,2,45,3,53, 27,48,17,19,26,22, 30,17,20,29,15,60, 19,55,30,23,37,49, 43,17,8,15,49,39, 43,53,13,32,34,24, 48,15,24,27,17,32, 17,40,22,27,33,3, 50,15,17,2,14,59, 4,17,42,56,46,24, 58,52,8,34,20,23, 54,11,51,16,36,30, 23,18,31,17,53,28, 59,51,13,1,9,50, 34,56,24,1,49,8, 5,3,52,45,9,51, 24,55,15,33,25,42, 11,20,8,47,12,17, 31,50,7,53,32,20, 48,52,57,24,3,33, 11,36,17,26,52,48, 15,31,23,6,59,37, 2,15,58,10,59,21, 46,23,30,47,5,3, 42,13,20,29,43,57, 38,48,14,3,11,5, 54,10,59,44,30,7, 1,6,57,29,48,7, 37,11,17,31,43,10, 24,17,4,54,30,10, 36,17,28,16,54,30, 50,17,13,27,4,39, 58,26,40,37,47,52, 50,21,10,25,38,8, 55,32,17,36,26,43, 60,8,32,28,46,30, 51,13,43,24,3,14, 7,32,54,50,30,37, 6,16,10,34,47,42, 29,36,27,18,59,46, 8,22,33,40,32,53, 60,12,56,37,55,43, 38,45,35,37,5,51, 43,12,59,30,57,29, 41,42,52,53,16,9, 45,8,32,49,15,52, 25,7,12,21,42,34, 13,1,23,56,54,33, 38,44,4,1,27,42, 35,26,58,52,45,16, 35,53,29,33,2,4, 45,5,14,21,59,12, 10,56,12,31,45,38, 31,55,36,24,8,38, 26,49,25,18,31,34, 49,44,33,28,56,14, 49,2,18,51,22,57, 47,32,48,12,38,2, 57,60,34,24,29,47, 24,38,58,1,40,28, 46,31,7,16,60,27, 27,43,58,5,16,56, 50,18,44,53,11,43, 29,59,13,10,54,28, 59,55,16,27,47,11, 28,7,16,37,36,22, 32,24,2,5,1,46, 47,18,6,45,34,42, 11,58,31,14,10,20, 15,49,42,5,45,35, 12,50,36,6,35,40, 49,47,39,31,15,23, 7,15,35,16,40,4, 7,22,34,12,38,53, 46,14,54,18,43,5, 52,48,53,58,23,36, 29,28,48,47,43,22, 39,54,43,36,17,35, 22,12,24,18,5,16, 28,50,47,24,40,52, 48,22,53,56,50,14, 54,38,53,31,37,34, 9,56,46,28,10,55, 47,22,13,30,31,57, 41,55,24,59,33,40, 55,45,48,41,5,38, 46,19,3,45,12,27, 25,13,10,43,35,48, 51,9,42,5,58,1, 54,2,26,5,44,16, 31,33,24,10,5,1, 24,17,46,57,16,39, 23,33,39,4,60,18, 51,42,4,54,1,40, 21,42,1,60,35,14, 13,50,38,32,44,29, 52,49,27,33,12,10, 6,4,51,7,21,15, 52,19,34,37,58,23, 59,44,29,5,51,57, 39,54,29,49,47,19, 37,20,33,46,7,56, 41,28,45,31,16,59, 47,24,29,55,53,23, 31,54,20,29,13,19, 40,42,32,12,21,17, 45,53,32,2,30,35, 54,19,5,58,56,21, 2,37,22,60,14,23, 40,52,38,16,7,41, 60,46,30,55,23,19, 49,7,47,25,20,44, 15,16,59,60,24,41, 23,30,43,10,15,57, 9,38,32,8,54,28, 39,40,33,52,19,30, 26,10,52,1,12,48, 56,7,46,60,41,12, 56,11,58,46,51,22, 33,36,12,35,10,14, 4,6,7,24,12,41, 29,49,54,51,16,34, 56,23,22,43,16,5, 10,60,42,9,33,12, 13,16,12,5,27,50, 48,46,9,1,36,4, 31,52,14,54,16,4, 2,18,54,22,30,26, 43,33,57,23,59,7, 41,26,51,14,24,23, 35,27,53,44,52,4, 28,23,42,29,44,34, 27,1,35,20,37,13, 2,4,23,37,14,51, 24,11,40,12,35,10, 51,5,23,7,14,21, 46,38,29,33,32,48, 52,23,40,51,44,21, 4,23,3,1,21,53, 22,8,30,15,47,25, 31,49,54,33,26,40, 18,11,29,44,47,56, 11,31,32,48,49,4, 20,53,47,50,22,27, 12,16,23,17,19,48, 19,53,40,3,31,20, 27,20,48,16,30,35, 28,51,56,6,24,43, 50,21,43,12,28,22, 5,32,40,58,37,34, 14,38,53,24,16,37, 14,30,50,41,47,23, 32,22,24,41,30,38, 28,14,29,2,31,32, 39,50,25,55,11,4, 55,25,4,11,29,39, 26,17,13,41,16,44, 30,19,57,41,56,47, 11,5,27,60,38,53, 42,7,11,34,59,41, 7,13,30,37,47,17, 25,40,12,60,30,41, 58,26,49,57,48,9, 27,57,41,38,28,24, 7,5,2,53,33,49, 22,34,24,23,5,60, 20,28,41,1,33,36, 20,51,42,3,52,46, 24,44,7,31,12,50, 28,45,41,22,57,25, 6,12,35,5,28,7, 24,34,53,45,23,13, 22,16,5,41,18,17, 57,30,7,25,40,26, 36,6,30,20,7,25, 50,9,18,11,6,17, 60,47,3,33,25,13, 44,37,56,29,47,35, 50,56,41,12,32,37, 8,36,14,32,30,7, 48,34,28,54,25,42, 33,24,36,9,14,23, 11,5,47,31,53,38, 5,16,30,25,58,20, 31,59,4,58,23,47, 22,10,18,55,15,31, 40,26,38,4,56,52, 53,59,39,45,22,57, 16,30,19,38,48,37, 11,39,47,18,13,26, 47,52,10,27,23,17, 36,58,9,10,56,24, 14,31,54,29,26,24, 45,27,35,40,5,9, 19,18,52,25,17,49, 21,10,47,6,5,33, 58,1,45,55,8,46, 38,54,48,23,2,46, 7,50,53,16,41,34, 5,25,31,13,1,33, 8,50,26,9,53,43, 53,60,48,20,58,11, 5,54,20,56,30,16, 43,4,60,59,6,33, 20,43,33,13,15,58, 12,60,54,7,55,50, 28,5,1,34,4,19, 21,52,34,26,2,32, 32,44,55,19,20,16, 4,30,56,21,22,1, 12,11,56,44,24,37, 17,54,4,51,32,26, 34,15,23,55,49,30, 55,25,41,42,43,7, 21,55,54,40,36,49, 56,16,34,41,35,32, 34,3,30,10,23,46, 2,57,32,43,16,37, 44,51,27,53,8,60, 19,60,50,24,47,33, 20,47,23,32,16,11, 22,7,4,21,28,56, 11,57,40,35,56,31, 59,28,25,41,57,38, 33,21,44,46,47,6, 15,9,41,13,37,42, 36,7,45,31,56,57, 10,52,50,57,25,60, 29,41,55,2,31,22, 15,45,54,25,42,41, 45,3,24,36,7,32, 29,19,41,22,37,59, 16,59,27,42,44,36, 56,44,41,40,8,53, 39,45,11,21,33,13, 16,40,45,59,43,13, 37,26,27,42,11,48, 2,50,59,38,49,1, 21,16,4,37,2,58, 20,16,18,7,44,21, 28,24,22,2,58,6, 5,48,30,55,52,19, 54,13,58,43,50,27, 36,53,55,13,60,14, 26,23,49,28,42,36, 54,40,42,17,47,12, 27,32,3,51,49,45, 35,42,59,18,30,14, 7,58,28,53,37,46, 30,12,6,50,35,31, 3,30,9,35,23,32, 29,57,15,45,59,6, 10,20,40,45,50,33, 37,58,20,38,48,32, 13,52,32,41,21,26, 23,15,57,24,47,25, 19,7,3,55,24,53, 20,26,56,18,34,51, 26,32,54,43,46,40, 31,41,51,39,58,29, 11,55,44,19,29,47, 49,53,44,12,24,45, 55,22,5,30,35,20, 12,15,44,34,51,19, 52,37,57,16,10,50, 40,23,1,18,35,8, 19,52,29,15,12,5, 32,17,9,14,24,7, 17,3,44,37,9,32, 32,42,43,25,28,33, 12,4,11,49,43,19, 1,60,26,41,28,54, 58,5,41,3,1,23, 32,40,42,21,10,5, 41,53,38,4,31,15, 34,42,43,46,27,17, 6,44,58,41,36,48, 24,26,51,25,14,23, 59,17,22,46,43,55, 9,60,21,16,41,34, 16,11,7,40,44,2, 46,60,5,10,28,3, 33,1,55,35,51,27, 39,6,29,60,51,23, 6,53,5,26,27,23, 5,27,19,26,15,33, 35,22,39,41,59,38, 28,4,1,45,53,3, 10,20,13,1,42,50, 11,52,22,23,36,59, 29,28,49,17,42,50, 49,36,14,26,35,10, 54,27,4,43,40,46, 7,51,55,41,58,46, 52,51,37,13,21,1, 45,2,35,9,50,31, 1,38,48,28,11,33, 60,57,59,13,12,22, 39,56,19,23,10,35, 4,19,14,10,44,28, 41,56,27,36,53,8, 23,33,51,38,48,21, 25,37,30,39,6,41, 13,42,52,58,2,54, 16,9,50,58,11,35, 58,43,51,14,17,4, 17,13,4,44,41,21, 52,23,42,17,55,49, 12,32,44,43,35,30, 8,10,24,33,45,48, 47,2,31,42,45,30, 12,5,15,51,58,29, 3,43,16,56,52,20, 50,44,12,55,52,54, 11,45,48,7,28,20, 32,55,59,41,58,35, 24,6,38,23,28,16, 51,34,25,60,42,32, 43,15,41,51,16,31, 8,32,44,36,45,55, 40,18,6,20,50,53, 20,59,19,54,15,8, 10,22,42,13,41,58, 55,31,46,44,41,7, 26,27,13,42,41,3, 41,14,37,5,40,27, 26,15,16,22,19,49, 17,25,45,38,1,59, 35,40,21,59,53,22, 60,32,25,36,52,4, 19,57,6,39,34,5, 44,35,50,41,9,7, 30,9,17,27,4,44, 13,42,38,49,53,29, 46,54,10,9,1,32, 23,43,3,21,9,18, 59,21,51,54,29,50, 32,28,6,10,11,40, 56,47,25,59,53,41, 52,5,34,57,15,41, 13,42,16,32,14,26, 20,43,39,11,53,17, 53,41,44,2,29,55, 46,45,16,40,27,3, 47,21,1,50,36,38, 22,57,37,9,25,56, 53,42,27,20,33,25, 36,42,32,5,13,51, 6,14,24,20,4,38, 47,54,18,6,12,37, 34,54,26,28,55,7, 37,43,34,20,12,42, 52,32,4,33,25,22, 57,58,18,31,43,52, 54,13,44,49,48,1, 60,29,34,24,21,59, 2,24,52,4,16,51, 24,16,38,5,39,35, 3,13,31,43,46,49, 13,1,38,21,52,4, 9,1,57,7,54,49, 44,42,37,56,19,20, 39,1,37,31,29,18, 46,48,30,14,29,51, 30,33,24,11,46,60, 43,33,14,31,35,13, 56,53,11,14,5,35, 4,42,58,26,7,40, 46,60,6,40,50,45, 28,51,55,18,52,8, 22,53,31,28,2,36, 5,23,51,3,1,24, 60,4,10,35,39,2, 21,26,40,54,9,52, 59,42,34,13,44,55, 45,37,29,4,43,18, 40,4,28,32,11,5, 54,21,6,34,36,22, 47,15,30,37,45,6, 10,34,4,6,25,40, 24,16,4,42,57,15, 51,36,53,29,18,15, 47,41,10,60,54,23, 51,40,37,23,48,28, 43,25,2,13,31,17, 22,32,46,12,25,31, 29,54,40,57,49,21, 33,18,23,8,17,53, 36,49,37,35,24,21, 2,24,34,50,38,37, 57,25,45,28,51,26, 19,48,43,1,34,44, 53,16,45,43,33,27, 40,17,23,43,27,58, 56,58,34,53,25,45, 53,13,3,1,12,59, 47,14,27,52,17,12, 15,26,12,33,48,13, 20,1,5,32,25,34, 8,54,50,60,23,12, 26,9,41,49,25,40, 52,13,6,24,8,31, 59,8,18,29,42,44, 38,14,21,15,3,20, 28,13,34,2,8,54, 30,49,27,37,12,44, 27,17,16,34,7,59, 51,35,59,7,20,2, 29,2,14,38,23,52, 5,21,9,56,18,36, 42,13,3,46,38,16, 58,15,59,30,38,46, 23,24,42,25,17,47, 57,44,21,16,58,6, 33,7,43,35,13,55, 47,5,34,28,2,50, 35,17,3,48,25,56, 32,46,1,60,24,23, 30,7,37,55,44,53, 47,38,18,14,29,44, 2,58,25,6,26,17, 24,36,19,33,7,11, 38,26,35,39,12,47, 3,12,46,5,47,8, 16,37,45,52,56,12, 55,42,10,43,45,54, 22,6,7,52,38,60, 13,3,51,17,29,25, 21,57,16,23,54,4, 15,13,57,53,40,17, 5,33,49,17,42,39, 43,33,14,36,5,44, 56,19,28,48,17,45, 38,50,7,29,15,14, 14,56,58,8,43,3, 60,6,22,3,24,54, 44,33,13,51,17,20, 50,53,57,10,58,22, 56,50,55,54,24,43, 1,8,14,28,33,43, 17,52,51,59,39,37, 9,38,56,1,31,46, 49,46,6,53,33,36, 25,28,30,33,51,11, 5,25,12,10,60,24, 37,36,56,27,42,23, 10,20,6,19,51,13, 60,58,49,32,20,34, 60,12,33,52,35,51, 16,2,27,47,23,53, 47,32,50,54,18,56, 20,27,43,16,19,4, 25,15,58,37,59,38, 25,4,18,57,21,38, 55,43,56,54,8,60, 53,17,38,4,47,37, 56,38,21,20,3,5, 19,40,7,13,22,47, 1,19,46,6,16,2, 6,59,42,27,1,5, 36,30,10,11,29,47, 9,39,37,49,43,41, 41,5,4,52,30,33]
repetidos = collections.Counter(numeros)
x = 0

for x in range(1,61):
    print(f'o número ,{x}, repetiu ,{repetidos[x]}, vezes.')


