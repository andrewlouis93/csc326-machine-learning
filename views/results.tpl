% rebase('base/base.tpl')

<form class="form-inherit" method="POST" action="/query">
  <div class="mdl-grid">
      <div class="mdl-cell mdl-cell--8-col">
        <div class="mdl-textfield mdl-js-textfield">
          <input id="query" class="mdl-textfield__input" type="text" name="query" />
          <label class="mdl-textfield__label" for="query">your search goes here...</label>
        </div>
      </div>
      <div class="mdl-cell mdl-cell--4-col">
        <input type="submit" />
      </div>
  </div>
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
