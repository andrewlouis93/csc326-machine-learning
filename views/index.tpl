% rebase('base/base.tpl')

<form method="POST" action="/query">
  <input name="query" />
  <input type="submit" />
</form>

<ul>
    % if results:
      % for it in results:
        <li>
          {{it[0]}} - {{it[1]}}
        </li>
      % end
    % end
</ul>
