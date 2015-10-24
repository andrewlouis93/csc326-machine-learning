% rebase('base/base.tpl')

<form class="results-search" method="GET" action="/">
  <div class="row">
    <div class="col-md-8 limited-padding">
      <div class="input-group input-group-lg search-ctr-results">
        <input type="text" name="keywords" class="form-control search-bar" value="{{query_str}}">
      </div>
    </div>
    <div class="col-md-4 limited-padding">
      <input type="submit" class="btn btn-lg btn-default westit-results" value="west it" />
    </div>
  </div>
</form>

% if results:
  % if logged_in:
  <div class="table-ctr-2-2">
  % else:
  <div class="table-ctr">
  % end
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
    <table id="results" class="row ref-table">
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

% if last_ten:
<div class="table-ctr-2-1">
  <div class="row table-titles">
    <div class="col-xs-12 col-sm-12 col-md-12 lead">
      <span class="thick-header">
        last 10
      </span>
    </div>
  </div>
  <table id="last_ten" class="row ref-table">
    <tbody>
  % for it in last_ten:
    <tr>
      <td class="col-xs-12 col-sm-12 col-md-12 lead">
        {{it}}
      </td>
    </tr>
  % end
  </tbody>
  </table>
</div>
<br/>
<br/>
% end
