FasdUAS 1.101.10   ��   ��    k             l     ��  ��     - INTERNAL FUNCTIONS:     � 	 	 * -   I N T E R N A L   F U N C T I O N S :   
  
 l     ��  ��    , &-	 � setKMVar(pKMVarName, pKMVarValue)     �   L - 	   "   s e t K M V a r ( p K M V a r N a m e ,   p K M V a r V a l u e )      l     ��  ��     -	 � bolToNum(pbolVar)     �   , - 	   "   b o l T o N u m ( p b o l V a r )      l     ��  ��     -	 � numToBol(pnumVar)     �   , - 	   "   n u m T o B o l ( p n u m V a r )      l     ��������  ��  ��        l     ����  r         m          � ! !  B  o      ���� 0 
strasradio 
strASRadio��  ��     " # " l     ��������  ��  ��   #  $ % $ l     �� & '��   & - '- SET POSIX FILE PATH FOR HTML FILE ---    ' � ( ( N -   S E T   P O S I X   F I L E   P A T H   F O R   H T M L   F I L E   - - - %  ) * ) l    +���� + r     , - , m     . . � / / � / U s e r s / s a m e n g l a n d e r / L i b r a r y / A p p l i c a t i o n   S u p p o r t / K e y b o a r d   M a e s t r o / K e y b o a r d   M a e s t r o   A c t i o n s / s a m h t m l f o r m / d i s p l a y . h t m l - o      ���� 0 strhtmlfile strHTMLFile��  ��   *  0 1 0 l     ��������  ��  ��   1  2 3 2 l     �� 4 5��   4 - '- SET KM VARS (Create if necessary) ---    5 � 6 6 N -   S E T   K M   V A R S   ( C r e a t e   i f   n e c e s s a r y )   - - - 3  7 8 7 l     ��������  ��  ��   8  9 : 9 l     �� ; <��   ; / )setKMVar("HTML Prompt File", strHTMLFile)    < � = = R s e t K M V a r ( " H T M L   P r o m p t   F i l e " ,   s t r H T M L F i l e ) :  > ? > l    @���� @ I    �� A���� 0 setkmvar setKMVar A  B C B m   	 
 D D � E E " A S _ H T M L _ F o r m _ F i l e C  F�� F o   
 ���� 0 strhtmlfile strHTMLFile��  ��  ��  ��   ?  G H G l     ��������  ��  ��   H  I J I l     ��������  ��  ��   J  K L K l     �� M N��   M I C- MUST SET RESULT BUTTON, IF USER PRESSES ESC BUTTON IS NOT SET ---    N � O O � -   M U S T   S E T   R E S U L T   B U T T O N ,   I F   U S E R   P R E S S E S   E S C   B U T T O N   I S   N O T   S E T   - - - L  P Q P l    R���� R I    �� S���� 0 setkmvar setKMVar S  T U T m     V V � W W $ H T M L   R e s u l t   B u t t o n U  X�� X m     Y Y � Z Z  T B D��  ��  ��  ��   Q  [ \ [ l     ��������  ��  ��   \  ] ^ ] l     �� _ `��   _ 2 ,- SET INITIAL VALUE FOR FORM FIELD NAMES ---    ` � a a X -   S E T   I N I T I A L   V A L U E   F O R   F O R M   F I E L D   N A M E S   - - - ^  b c b l    d���� d I    �� e���� 0 setkmvar setKMVar e  f g f m     h h � i i  A S R a d i o g  j�� j o    ���� 0 
strasradio 
strASRadio��  ��  ��  ��   c  k l k l     ��������  ��  ��   l  m n m l    � o p q o O     � r s r k   $  t t  u v u l  $ $��������  ��  ��   v  w x w l  $ $�� y z��   y . (- EXECUTE MACRO TO DISPLAY HTML FORM ---    z � { { P -   E X E C U T E   M A C R O   T O   D I S P L A Y   H T M L   F O R M   - - - x  | } | I  $ )�� ~��
�� .coredoscnull���     ctxt ~ m   $ %   � � �  s a m h t m l f o r m��   }  � � � l  * *��������  ��  ��   �  � � � l  * *�� � ���   � ? 9- AppleScript will wait here until User submits form  ---    � � � � r -   A p p l e S c r i p t   w i l l   w a i t   h e r e   u n t i l   U s e r   s u b m i t s   f o r m     - - - �  � � � l  * *��������  ��  ��   �  � � � l  * *��������  ��  ��   �  � � � l  * *�� � ���   � 1 +- OK, FORM HAS BEEN SUBMITTED, GET DATA ---    � � � � V -   O K ,   F O R M   H A S   B E E N   S U B M I T T E D ,   G E T   D A T A   - - - �  � � � l  * *��������  ��  ��   �  � � � l  * *�� � ���   �  - GET BUTTON CLICKED ---    � � � � 0 -   G E T   B U T T O N   C L I C K E D   - - - �  � � � l  * *�� � ���   � F @		If form was closed by user pressing ESC, no button was clicked    � � � � � 	 	 I f   f o r m   w a s   c l o s e d   b y   u s e r   p r e s s i n g   E S C ,   n o   b u t t o n   w a s   c l i c k e d �  � � � l  * *�� � ���   � < 6		and the KM var "HTML Result Button" will NOT be set.    � � � � l 	 	 a n d   t h e   K M   v a r   " H T M L   R e s u l t   B u t t o n "   w i l l   N O T   b e   s e t . �  � � � l  * *�� � ���   � 6 0		But we will treat it as if the user cancelled.    � � � � ` 	 	 B u t   w e   w i l l   t r e a t   i t   a s   i f   t h e   u s e r   c a n c e l l e d . �  � � � l  * *�� � ���   � O I		That's why before form was submitted, the "HTML Result Button" variable    � � � � � 	 	 T h a t ' s   w h y   b e f o r e   f o r m   w a s   s u b m i t t e d ,   t h e   " H T M L   R e s u l t   B u t t o n "   v a r i a b l e �  � � � l  * *�� � ���   �  		was set to "TBD"    � � � � $ 	 	 w a s   s e t   t o   " T B D " �  � � � r   * 2 � � � n   * 0 � � � 1   . 0��
�� 
MKvl � 4   * .�� �
�� 
MKvr � m   , - � � � � � $ H T M L   R e s u l t   B u t t o n � o      ���� 0 strkmbutton strKMButton �  � � � I  3 <�� ���
�� .ascrcmnt****      � **** � b   3 8 � � � m   3 6 � � � � �  R e s u l t   B u t t o n :   � o   6 7���� 0 strkmbutton strKMButton��   �  � � � l  = =��������  ��  ��   �  � � � Z   = } � ��� � � l  = B ����� � =   = B � � � o   = >���� 0 strkmbutton strKMButton � m   > A � � � � �  S a v e��  ��   � l  E a � � � � k   E a � �  � � � l  E E��������  ��  ��   �  � � � r   E O � � � n   E M � � � 1   K M��
�� 
MKvl � 4   E K�� �
�� 
MKvr � m   G J � � � � �  A S R a d i o � o      ���� 0 
strasradio 
strASRadio �  � � � l  P P��������  ��  ��   �  � � � l  P P�� � ���   � / )- INSERT YOUR PROCESSING OF FORM DATA ---    � � � � R -   I N S E R T   Y O U R   P R O C E S S I N G   O F   F O R M   D A T A   - - - �  � � � l  P P��������  ��  ��   �  � � � r   P W � � � m   P S � � � � �  S U C C E S S � o      ���� 0 stralerttitle strAlertTitle �  � � � r   X _ � � � m   X [ � � � � � : V a r i a b l e s   U p d a t e d   v i a   K M   F o r m � o      ���� 0 stralertmsg strAlertMsg �  � � � l  ` `��������  ��  ��   �  ��� � l  ` `��������  ��  ��  ��   �   GET KM vars, & process    � � � � .   G E T   K M   v a r s ,   &   p r o c e s s��   � l  d } � � � � k   d } � �  � � � l  d d��������  ��  ��   �  � � � I  d k�� ���
�� .ascrcmnt****      � **** � m   d g � � � � �  U s e r   C a n c e l e d��   �    r   l s m   l o � , * * *   U S E R   C A N C E L L E D   * * * o      ���� 0 stralerttitle strAlertTitle  r   t {	 m   t w

 �  W h a t   N o w ?	 o      ���� 0 stralertmsg strAlertMsg �� l  | |�������  ��  �  ��   � A ; User Canceled, so terminate script, or handle cancellation    � � v   U s e r   C a n c e l e d ,   s o   t e r m i n a t e   s c r i p t ,   o r   h a n d l e   c a n c e l l a t i o n � �~ l  ~ ~�}�|�{�}  �|  �{  �~   s m     !�                                                                                  KM*E  alis    �  Untitled                       BD ����Keyboard Maestro Engine.app                                    ����            ����  
 cu             MacOS   O/:Applications:Keyboard Maestro.app:Contents:MacOS:Keyboard Maestro Engine.app/   8  K e y b o a r d   M a e s t r o   E n g i n e . a p p    U n t i t l e d  LApplications/Keyboard Maestro.app/Contents/MacOS/Keyboard Maestro Engine.app  / ��   p , & application "Keyboard Maestro Engine"    q � L   a p p l i c a t i o n   " K e y b o a r d   M a e s t r o   E n g i n e " n  l     �z�y�x�z  �y  �x    l  � � I  � ��w
�w .sysodisAaleR        TEXT o   � ��v�v 0 stralerttitle strAlertTitle �u
�u 
mesS o   � ��t�t 0 stralertmsg strAlertMsg �s
�s 
as A l 
 � ��r�q m   � ��p
�p EAlTcriT�r  �q   �o�n
�o 
btns J   � �   !"! m   � �## �$$  C a n c e l" %�m% m   � �&& �''  I g n o r e�m  �n     last button is default    �(( .   l a s t   b u t t o n   i s   d e f a u l t )*) l     �l�k�j�l  �k  �j  * +,+ l     �i-.�i  - : 4- LOG VARS AFTER FORM WAS SUBMITTED OR CANCELLED ---   . �// h -   L O G   V A R S   A F T E R   F O R M   W A S   S U B M I T T E D   O R   C A N C E L L E D   - - -, 010 l  � �2�h�g2 I  � ��f3�e
�f .ascrcmnt****      � ****3 o   � ��d�d 0 
strasradio 
strASRadio�e  �h  �g  1 454 l     �c�b�a�c  �b  �a  5 676 l     �`89�`  8  - INTERNAL FUNCTION   9 �:: & -   I N T E R N A L   F U N C T I O N7 ;<; i     =>= I      �_?�^�_ 0 setkmvar setKMVar? @A@ o      �]�] 0 
pkmvarname 
pKMVarNameA B�\B o      �[�[ 0 pkmvarvalue pKMVarValue�\  �^  > k     ,CC DED l     �Z�Y�X�Z  �Y  �X  E FGF l     �WHI�W  H : 4log ("setKMVar: " & pKMVarName & ": " & pKMVarValue)   I �JJ h l o g   ( " s e t K M V a r :   "   &   p K M V a r N a m e   &   " :   "   &   p K M V a r V a l u e )G KLK l     �V�U�T�V  �U  �T  L MNM l    *OPQO O     *RSR k    )TT UVU l   �S�R�Q�S  �R  �Q  V WXW Q    'YZ[Y l   \]^\ k    __ `a` r    bcb o    �P�P 0 pkmvarvalue pKMVarValuec n      ded 1    �O
�O 
MKvle 4    �Nf
�N 
MKvrf o   
 �M�M 0 
pkmvarname 
pKMVarNamea g�Lg l   �K�J�I�K  �J  �I  �L  ] 6 0 to set variable, will error if it doesn't exist   ^ �hh `   t o   s e t   v a r i a b l e ,   w i l l   e r r o r   i f   i t   d o e s n ' t   e x i s tZ R      �H�G�F
�H .ascrerr ****      � ****�G  �F  [ l   'ijki I   '�E�Dl
�E .corecrel****      � null�D  l �Cmn
�C 
koclm m    �B
�B 
MKvrn �Ao�@
�A 
prdto K    #pp �?qr
�? 
pnamq o    �>�> 0 
pkmvarname 
pKMVarNamer �=s�<
�= 
MKvls o     !�;�; 0 pkmvarvalue pKMVarValue�<  �@  j   Make & Set Variable   k �tt (   M a k e   &   S e t   V a r i a b l eX u�:u l  ( (�9�8�7�9  �8  �7  �:  S m     vv�                                                                                  KM*E  alis    �  Untitled                       BD ����Keyboard Maestro Engine.app                                    ����            ����  
 cu             MacOS   O/:Applications:Keyboard Maestro.app:Contents:MacOS:Keyboard Maestro Engine.app/   8  K e y b o a r d   M a e s t r o   E n g i n e . a p p    U n t i t l e d  LApplications/Keyboard Maestro.app/Contents/MacOS/Keyboard Maestro Engine.app  / ��  P 	  KM   Q �ww    K MN x�6x l  + +�5�4�3�5  �4  �3  �6  < yzy l     �2�1�0�2  �1  �0  z {|{ l     �/}~�/  } 2 ,- bolToNum() Convert Boolean to Number (1/0)   ~ � X -   b o l T o N u m ( )   C o n v e r t   B o o l e a n   t o   N u m b e r   ( 1 / 0 )| ��� i    ��� I      �.��-�. 0 boltonum bolToNum� ��,� o      �+�+ 0 pbolvar pbolVar�,  �-  � k     �� ��� l     �*�)�(�*  �)  �(  � ��� Z     ���'�� o     �&�& 0 pbolvar pbolVar� r    ��� m    �%�% � o      �$�$ 0 nvar nVar�'  � r   
 ��� m   
 �#�#  � o      �"�" 0 nvar nVar� ��� l   �!� ��!  �   �  � ��� L    �� o    �� 0 nvar nVar� ��� l   ����  �  �  �  � ��� l     ����  �  �  � ��� l     ����  � , &- numToBol() Convert Number to Boolean   � ��� L -   n u m T o B o l ( )   C o n v e r t   N u m b e r   t o   B o o l e a n� ��� i    ��� I      ���� 0 numtobol numToBol� ��� o      �� 0 pnumvar pnumVar�  �  � k     �� ��� l     ����  �  �  � ��� Z     ����� =     ��� l    ���� c     ��� o     �� 0 pnumvar pnumVar� m    �

�
 
long�  �  � m    �	�	  � r    ��� m    	�
� boovfals� o      �� 0 bolvar bolVar�  � r    ��� m    �
� boovtrue� o      �� 0 bolvar bolVar� ��� l   ����  �  �  � ��� L    �� o    �� 0 bolvar bolVar� �� � l   ��������  ��  ��  �   � ���� l     ��������  ��  ��  ��       �������   .�
����������������  � ���������������������������������� 0 setkmvar setKMVar�� 0 boltonum bolToNum�� 0 numtobol numToBol
�� .aevtoappnull  �   � ****�� 0 
strasradio 
strASRadio�� 0 strhtmlfile strHTMLFile�� 0 strkmbutton strKMButton�� 0 stralerttitle strAlertTitle�� 0 stralertmsg strAlertMsg��  ��  ��  ��  ��  ��  ��  � ��>���������� 0 setkmvar setKMVar�� ����� �  ������ 0 
pkmvarname 
pKMVarName�� 0 pkmvarvalue pKMVarValue��  � ������ 0 
pkmvarname 
pKMVarName�� 0 pkmvarvalue pKMVarValue� 
v������������������
�� 
MKvr
�� 
MKvl��  ��  
�� 
kocl
�� 
prdt
�� 
pnam�� 
�� .corecrel****      � null�� -� ' �*�/�,FOPW X  *������� 	OPUOP� ������������� 0 boltonum bolToNum�� ����� �  ���� 0 pbolvar pbolVar��  � ������ 0 pbolvar pbolVar�� 0 nvar nVar�  �� � kE�Y jE�O�OP� ������������� 0 numtobol numToBol�� ����� �  ���� 0 pnumvar pnumVar��  � ������ 0 pnumvar pnumVar�� 0 bolvar bolVar� ��
�� 
long�� ��&j  fE�Y eE�O�OP� �����������
�� .aevtoappnull  �   � ****� k     ���  ��  )��  >��  P��  b��  m�� �� 0����  ��  ��  �  � #  �� .�� D�� V Y h ���� ����� ��� � � ��� ��� �
��������#&������ 0 
strasradio 
strASRadio�� 0 strhtmlfile strHTMLFile�� 0 setkmvar setKMVar
�� .coredoscnull���     ctxt
�� 
MKvr
�� 
MKvl�� 0 strkmbutton strKMButton
�� .ascrcmnt****      � ****�� 0 stralerttitle strAlertTitle�� 0 stralertmsg strAlertMsg
�� 
mesS
�� 
as A
�� EAlTcriT
�� 
btns�� 
�� .sysodisAaleR        TEXT�� ��E�O�E�O*��l+ O*��l+ O*��l+ O� ]�j O*��/�,E�Oa �%j O�a   !*�a /�,E�Oa E` Oa E` OPY a j Oa E` Oa E` OPOPUO_ a _ a a a a a  lva ! "O�j � ���  C a n c e l��  ��  ��  ��  ��  ��  ��  ascr  ��ޭ