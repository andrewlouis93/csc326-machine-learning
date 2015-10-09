% rebase('base/base.tpl')


% if results:
<div class="table-ctr">
  <div class="row table-titles">
    <div class="col-xs-6 col-sm-6 col-md-6 lead">
      <span class="thick-header">
        word
      </span>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 lead">
      <span class="thick-header">
        count
      </span>
    </div>
  </div>
  <table id="history" class="row ref-table">
    <tbody>
  % for res in results:
    <tr>
      <td class="col-xs-6 col-sm-6 col-md-6 lead">
        {{res[0]}}
      </td>
      <td class="col-xs-6 col-sm-6 col-md-6 lead">
        <div class="count-badge">
          {{res[1]}}
        </div>
      </td>
    </tr>
  % end
  </tbody>
  </table>
</div>
% end
