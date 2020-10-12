# b1
chuoi = input ( "nhap chuoi:" )
def  manual_replace ( s , char , index ):
    trả về  s [: index ] +  char  +  s [ index  + 1 :]
print ( manual_replace ( chuoi , "$" , 0 ))

# b2
chuoi = input ( "nhap chuoi:" )
def  remove_char_m ( str , n ):
      phan_dau = str [: n ]
      phan_cuoi = str [ n + 1 :]
      return  phan_dau  +  phan_cuoi
print ( remove_char_m ( chuoi , int ( input ( "thu tu muon xoa:" ))))

# b3
chuoi  =  input ( "nhap chuoi:" )
def  Even_values_string ( str ):
  ketqua  =  "" 
  for  i  in  range ( len ( str )):
    nếu  tôi  %  2  ! =  0 :
      ketqua  =  ketqua  +  str [ i ]
  trả lại  ketqua
print ( Even_values_string ( chuoi ))

#B 4
chuoi  =  input ( "nhap chuoi:" )
def  dau_va_duoi ( str ):
  nếu  len ( str ) <  2 :
    return  "chuoi rong"
  trả về  str [ 0 : 2 ] +  str [ - 2 :]
print ( dau_va_duoi ( chuoi ))

# b5
chuoi  =  input ( "nhap chuoi:" )
print ( "ki tu lon nhat cua chuoi:" , max ( chuoi ))
print ( "ki tu nho nhat cua chuoi:" , min ( chuoi ))

# b6
chuoi  =  input ( "nhap chuoi:" )
print ( chuoi . swapcase ())