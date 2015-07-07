"""obj_from_name: Get aospy objects given their name string"""
import aospy
from aospy_user import projs, regions, variables


def to_iterable(obj):
    """Return the object if already iterable, otherwise return it as a list."""
    try:
        zip([], obj)
    except TypeError:
        return [obj]
    else:
        return obj


def to_proj(proj):
    """Convert string of an aospy.Proj name to an aospy.Proj instance."""
    orig_type = type(proj)
    if isinstance(proj, aospy.proj.Proj):
        return proj

    elif isinstance(proj, str):
        try:
            return getattr(projs, proj)
        except AttributeError:
            raise AttributeError('Not a recognized Proj name: %s' % proj)

    elif isinstance(proj, (list, tuple)):
        proj = [to_proj(pr) for pr in proj]
        if orig_type is list:
            return proj
        else:
            return tuple(proj)

    else:
        raise TypeError


def to_model(model, proj):
    """Convert string of a Model name to a Model instance."""
    orig_type = type(model)
    proj = to_proj(proj)

    if isinstance(model, aospy.model.Model):
        return model

    elif isinstance(model, str):
        if model == 'all':
            model = proj.models.values()
        elif model == 'default':
            model = proj.default_models.values()
        else:
            model = proj.models[model]
        return model

    elif isinstance(model, (list, tuple)):
        model = [to_model(mod, pr) for (mod, pr)
                 in zip(model, aospy.io.to_dup_list(proj, len(model)))]
        if orig_type is tuple:
            model = tuple(model)
        return model

    else:
        raise TypeError


def to_run(run, model, proj):
    """Convert string matching an aospy.run name to an aospy.run instance."""
    orig_type = type(run)
    proj = to_proj(proj)
    model = to_model(model, proj)

    if isinstance(run, aospy.run.Run):
        return run

    elif isinstance(run, str):
        if run == 'default':
            return model.default_runs.values()
        elif run == 'all':
            return model.runs
        else:
            run = model.runs[run]
            return run

    elif isinstance(run, dict):
        # Assume run(s) is/are key(s), not value(s).
        vals = run.values()
        keys = to_run(run.keys(), model, proj)
        return dict(zip(keys, vals))

    elif isinstance(run, (list, tuple)):
        run = [to_run(rn, mod, pr) for (rn, mod, pr)
               in zip(run, aospy.io.to_dup_list(model, len(run)),
                      aospy.io.to_dup_list(proj, len(run)))]
        if orig_type is tuple:
            run = tuple(run)
        return run

    else:
        raise TypeError


def to_var(var):
    """Convert string of an aospy.var name to an aospy.var instance."""
    if isinstance(var, aospy.var.Var):
        var_out = var

    elif isinstance(var, str):
        try:
            var_out = getattr(variables, var)
        except AttributeError:
            raise AttributeError('Not a recognized Var name: %s' % var)

    elif isinstance(var, (list, tuple)):
        var_out = [to_var(v) for v in var]
        if isinstance(var, tuple):
            var_out = tuple(var_out)

    else:
        raise TypeError

    return var_out


def to_region(region, proj=False):
    """Convert string of an aospy.Region name to an aospy.Region instance."""
    if isinstance(region, aospy.region.Region):
        return region

    elif isinstance(region, bool) or region is None:
        return region

    elif isinstance(region, str):
        if proj and region == 'all':
            return proj.regions
        else:
            return getattr(regions, region)

    elif isinstance(region, (list, tuple)):
        region_out = [to_region(r, proj=proj) for r in region]
        if isinstance(region, tuple):
            region_out = tuple(region_out)
        return region_out

    else:
        raise TypeError
