 '<td>'.html_escape($_patient->first_name.' '.$_patient->last_name).'</td>'.
              '<td>'.html_escape($_patient->fname).'</td>'.
              '<td>'.html_escape($_patient->phone).'</td><td>';
              if(isset($_patient->birth_date))echo ((int)date('Y'))-((int)date('Y',$_patient->birth_date));else echo ''; echo'</td><td>';
              if($_patient->gender) echo 'M' ;else echo 'F'; echo '</td>'.
              '<td class="hidden-print">'.$actions.'</td>'.
            '</tr>';
